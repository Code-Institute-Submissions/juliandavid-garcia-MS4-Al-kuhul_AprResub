from django.shortcuts import render
from .models import Review

# Create your views here.

def review(request):
    """ A view to return the review page """
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'review/review.html', context)

  
    
