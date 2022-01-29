from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from profiles.models import UserProfile

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def product_reviews(request, review_id):

    reviews = Review.objects.filter(product=review_id)
    product = get_object_or_404(Product, pk=review_id)
    #profile = UserProfile.objects.get(user=request.user)
    
    #reviews for the product
    #product_review = product.review.all()

    #if product_review.exists():
    #    any_reviews = True
    #else:
    #    any_reviews = False

    #if request.user.is_authenticated:
        #profile = UserProfile.objects.get(user=request.user)
        #user_reviewed = product_review.filter(user_profile=profile).exists()
    #else:
        #user_reviewed = False

    context = {
        'reviews': reviews,
        'product': product,
        #'profile': profile,
        #'any_reviews': any_reviews,
        #'user_reviewed': user_reviewed,
    }
    
    return render(request, 'products/reviews.html', context)
    

@login_required     
def add_review(request, review_id):
    """ Add a review to the product """
    reviews = Review.objects.filter(product=review_id)
    product = get_object_or_404(Product, pk=review_id)
    profile = UserProfile.objects.get(user=request.user)

    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_form = form.save(commit=False)
            review_form.product = product
            review_form.user_profile = profile
            review_form = review_form.save()
            messages.success(request, 'Your review has been successfully added!')
            return redirect(reverse('product-reviews', args=[product.id]))
        else:
             message.error(request, 'Fail to add the review. please ensure the ##form is valid.')
    
    else:
        form = ReviewForm()

    template = 'products/add_review.html'
    context = { 
       'form': form,
       'product': product,
       'profile': profile,
         }

    return render(request, template, context)



def edit_review(request, review_id):
    """ Edit a review of a product """

    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        # check if form is valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product review!')
            return redirect(reverse('profile'))
        # form is not valid
        else:
            messages.error(request, 'Failed to update product review.' +
                           'Please ensure the form is valid.')
    # get form
    else:
        form = ReviewForm(instance=review)
        messages.info(request, 'You are editing your review for' +
                      f'{review.product}')

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review of a product """

    # get the review and delete it
    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    review.delete()
    messages.success(request, 'Product review deleted!')
    return redirect(reverse('profile'))



def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
    	form = CommentForm(request.POST)

    	if form.is_valid():
    		comment = form.save(commit=False)
    		comment.post = post
    		comment.save()

    		return redirect('post_detail', slug=post.slug)
    else:
    	form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})






def review_detail(request, review_id):
    """ A view that shows individual reviews  """

    Review = get_object_or_404(Review, pk=review_id)

    if request.method == 'GET':
        profile = UserProfile.objects.get(user=request.user)
        form = ReviewForm(request.GET)
        form_data = {
            'review': request.GET['review'],
        }
        productreview_form = ReviewForm(form_data)
        # check if form is valid
        if productreview_form.is_valid():
            context = {
                'reviews': reviews,
                    }
    
    return render(request, 'review_detail.html', context)
    