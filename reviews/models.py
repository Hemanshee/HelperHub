from django.db import models
from django.conf import settings
from helpers.models import Helper

# Create your models here.

user = settings.AUTH_USER_MODEL

class Review(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    helper = models.ForeignKey(Helper, on_delete=models.CASCADE)

    rating = models.IntegerField()  # 1 to 5
    comment = models.TextField()

    def __str__(self):
        return f"{self.user} rated {self.helper}"
