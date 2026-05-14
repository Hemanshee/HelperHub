from django.db import models
from django.conf import settings
from helpers.models import Helper

# Create your models here.
user = settings.AUTH_USER_MODEL

class Booking(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    helper = models.ForeignKey(Helper, on_delete=models.CASCADE)

    service_type = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    status = models.CharField(max_length=20, default='pending')
