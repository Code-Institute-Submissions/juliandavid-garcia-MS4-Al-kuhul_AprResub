from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm
from .models import Review
# Create your views here.


def reviews(request):
    """ A view that renders the views contents page """

    return render(request, 'review/reviews.html')
      
def add_review(request):
    """ Add a review to the product """
    if request.method == 'POST':
        form = ReviewForm(request.POST, request)
        if form.is_valid():
            form.save()
            message.success(request, 'Secuessfully added your reviews!')
            return redirect(reverse('add_review'))
        else:
            messages.error(request,'Failed to add your review. Make sure the form is valid.')
    else:
        form = ReviewForm()

    template = 'review/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)