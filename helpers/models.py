from django.db import models
from django.conf import settings

# Create your models here.

user = settings.AUTH_USER_MODEL

class Helper(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    skills = models.CharField(max_length=200)
    experience = models.IntegerField()
    price_per_day = models.IntegerField()
    location = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    profile_pic = models.ImageField(upload_to='helpers/', null=True, blank=True)


    def __str__(self):
        return self.name
    
    # Auto update rating Function

    def update_rating(self):
        reviews = self.review_set.all()

        if  reviews.exists():
            total = sum(review.rating for review in reviews)
            self.rating = round(total / reviews.count(), 1)  # 1 decimal exist
        
        else :
            self.rating = 0

        self.save()