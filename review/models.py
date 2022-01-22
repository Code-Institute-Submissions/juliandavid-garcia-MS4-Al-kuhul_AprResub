from django.db import models

# Create your models here.

class Reviews(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='review')
    product = models.ForeignKey(Product, models.CASCADE)
    comment = models.TextField(max_length=300)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.id)