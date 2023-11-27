from django.urls import path

from .views import CustomerAPIView

app_name = 'customer'

urlpatterns = [
    path('customer_register', CustomerAPIView.as_view(), name='register'),
]
