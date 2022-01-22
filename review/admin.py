from django.contrib import admin
from .models import Product, Category, Order, OrderLineItem, UserProfile, Review,
# Register your models here.
@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id','user_profile','product','rate','created_at']
    readonly_fields = ['created_at',]