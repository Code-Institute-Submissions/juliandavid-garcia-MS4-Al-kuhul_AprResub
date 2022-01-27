def add_review(request, product_id):
#    """ Add a review to the product """

    reviews = Review.objects.filter(pk=review_id)

    if request.method == 'POST':
        profile = UserProfile.objects.get(user=request.user)
        form = ReviewForm(request.POST, request)

        form_data = {
            'review': request.POST['review'],
        }

        form = ReviewForm(form_data)
        # check if form is valid
        if  form.is_valid():
            productreview = form.save(commit=False)
            productreview.user_profile = profile
            productreview.product = product
            productreview.review = review
            productreview.save()
            messages.success(request, 'Successfully added product review!')
            return redirect(reverse('product_detail'))
        # form is not valid  
        else:
            messages.error(request, 'Failed to add product review. ' +
                           'Please ensure the form is valid.')
    else:
        # check if the user has already made a review
        # for this product previously
        # if so redirect back to product page with an error message
        profile = UserProfile.objects.get(user=request.user)
        product_reviews = product.reviews.all()
        if product_reviews.filter(user_profile=profile).exists():
            messages.error(request, "You have already reviewed " +
                           "this product. You can update your " +
                           "review from below or your profile!")
            return redirect(reverse('product-reviews', args=[product.id]))
        else:
            form = ReviewForm()

    template = 'products/reviews.html'
    context = {
        'user': user,
        'form': form,
        'product': product,
    }

    return render(request, template, context)