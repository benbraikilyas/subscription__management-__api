from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from subscriptions.views import CustomerViewSet, ServiceViewSet, SubscriptionViewSet, PaymentViewSet
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Subscription Management API",
        default_version='v1',
        description="This is the API for managing subscriptions, payments, and customers.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('subscriptions.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    path('admin/', admin.site.urls),
    path('', include('subscriptions.urls')),
]