from django.db import models
from django.conf import settings
from bookings.models import Booking

# Create your models here.

user = settings.AUTH_USER_MODEL

class Payment(models.Model):
    user = models.ForeignKey(user , on_delete=models.CASCADE)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)

    amount = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20 ,default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
