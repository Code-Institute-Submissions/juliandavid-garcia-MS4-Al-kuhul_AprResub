from django.db import models
from profiles.models import UserProfile
from products.models import Product



# Create your models here.

class Review(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='Review')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    review = models.TextField(max_length=400, null=False, blank=False)
    

