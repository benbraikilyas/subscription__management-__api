# subscriptions/test/test_subscription.py

from rest_framework.test import APITestCase
from subscriptions.models import Service, Customer, Subscription
from django.contrib.auth.models import User
from rest_framework import status

class SubscriptionTests(APITestCase):
    def setUp(self):
        # إنشاء مستخدم
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # إنشاء عميل
        self.customer = Customer.objects.create(name="Test Customer", email="test@example.com")
        
        # إنشاء خدمة مع تعيين قيمة لـ price
        self.service = Service.objects.create(
            name="Test Service", 
            description="Test Service Description", 
            price=10.00  # التأكد من إضافة قيمة السعر هنا
        )
    
    def test_create_subscription(self):
        # تسجيل الدخول
        self.client.login(username='testuser', password='testpassword')
        
        # بيانات الاشتراك
        data = {
            "customer": self.customer.id,
            "service": self.service.id,
            "start_date": "2025-04-10",
            "end_date": "2025-05-10"
        }
        
        # إرسال طلب POST لإنشاء الاشتراك
        response = self.client.post('/subscription_management_api/subscriptions/', data, format='json')
        
        # التحقق من حالة الاستجابة
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['customer'], self.customer.id)
    
    def test_subscription_email_sent(self):
        # تحقق من إرسال البريد الإلكتروني هنا (قيد التنفيذ)
        pass
