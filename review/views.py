

from django.shortcuts import render

# Create your views here.

def review(request):
    """ A view to return the review page """

    return render(request, 'review/review.html')

    
 def view_bag(request):
    """ A view that renders the review contents page """

    return render(request, 'bag/bag.html')   
    
