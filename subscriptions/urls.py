from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ServiceViewSet, SubscriptionViewSet, PaymentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('subscriptions/', views.subscriptions_page, name='subscriptions'),
]