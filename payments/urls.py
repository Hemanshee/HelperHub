from django.urls import path
from .views import make_payment, payment_success

urlpatterns = [
    path('payment/<int:booking_id>/', make_payment, name='make_payment'),
    path('success/', payment_success, name='payment_success'),
]