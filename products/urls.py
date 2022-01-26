from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
<<<<<<< HEAD
    path('reviews', views.reviews, name='reviews'),
    path('review_detail/', views.review_detail, name='review_detail'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review')
    
=======
    path('reviews/', views.reviews, name='reviews'),
    path('<int:product_id>/', views.review_detail, name='review_detail'),
    path('add_review/', views.add_review, name='add_review'),
>>>>>>> 43f8d2346d10dc797a3222359eb43475790ba66f
]
