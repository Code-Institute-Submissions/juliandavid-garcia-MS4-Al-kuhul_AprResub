from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ReviewForm
# Create your views here.

def review(request):

    review_form = ReviewForm()
    template = 'review/review.html'
    context = {
        'review_form': review_form,
    }

    return render(request, template, reverse, context)

  
    
