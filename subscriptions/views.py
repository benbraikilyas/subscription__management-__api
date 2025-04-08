from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from .models import Customer, Service, Subscription, Payment
from .serializers import CustomerSerializer, ServiceSerializer, SubscriptionSerializer, PaymentSerializer
from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError
from django.shortcuts import render


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['name', 'email']
    search_fields = ['^name', '=email']
    pagination_class = StandardResultsSetPagination


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['start_date', 'end_date']

    def perform_create(self, serializer):
        subscription = serializer.save()
        self.send_subscription_email(subscription.Customer.email)

    def send_subscription_email(self, customer_email):
        subject = 'Your subscription has been successfully confirmed'
        message = 'Thank you for subscribing to our service. Updates will be sent soon.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [customer_email]

        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            # Log the error or handle it appropriately
            print(f"Failed to send email: {e}")


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


def subscriptions_page(request):
    return render(request, 'subscriptions/subscriptions.html')


# Endpoint to create subscription via API
@api_view(['POST'])
def create_subscription(request):
    if request.method == 'POST':
        # Get the data from the request
        customer_name = request.data.get('customer_name')
        email_address = request.data.get('email_address')
        subscription_plan = request.data.get('subscription_plan')
        billing_cycle = request.data.get('billing_cycle')

        # Validate the data
        if not customer_name or not email_address or not subscription_plan or not billing_cycle:
            return Response({'error': 'All fields are required!'}, status=status.HTTP_400_BAD_REQUEST)

        if not validate_email(email_address):
            return Response({'error': 'Invalid email address!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create a new subscription in the database
            subscription = Subscription.objects.create(
                customer_name=customer_name,
                email_address=email_address,
                subscription_plan=subscription_plan,
                billing_cycle=billing_cycle
            )

            # Send a confirmation email to the customer
            send_subscription_email(email_address)

            return Response({'message': 'Subscription created successfully!'}, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response({'error': f'Validation error: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def validate_email(email):
    """Validate email format"""
    from django.core.validators import validate_email
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def send_subscription_email(customer_email):
    """Send a confirmation email to the customer"""
    subject = 'Your subscription has been successfully confirmed'
    message = 'Thank you for subscribing to our service. Updates will be sent soon.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]

    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        print(f"Failed to send email: {e}")
