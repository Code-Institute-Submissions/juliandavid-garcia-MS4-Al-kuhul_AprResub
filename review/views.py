from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm
from .models import Review
# Create your views here.


def reviews(request):
    """ A view that renders the bag contents page """

    return render(request, 'review/reviews.html')
      
def add_review(request):
    
    form = ReviewForm()
    template = 'review/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)