from django.contrib import admin
from .models import Review
# Register your models here.
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'user_profile',
        'product',
        'review',
    ]

    ordering = ('product',)

admin.site.register(Review, ReviewAdmin)

