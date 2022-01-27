from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    #path('reviews', views.reviews, name='reviews'),
    #path('review_detail/', views.review_detail, name='review_detail'),
    path('add_review/<int:review_id>/', views.add_review, name='add_review'),
    path("reviews/<int:review_id>/", views.product_reviews, name="product-reviews"),
]
