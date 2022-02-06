from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile

# Create your views here.
from django.views import generic
from .models import Post
from .forms import CommentForm, PostForm
from profiles.models import UserProfile

def blog(request):


    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)


# change the post detail view

def post_detail(request, post_id):

    post = Post.objects.get(pk=post_id)
	
    if request.method == 'POST':
    	form = CommentForm(request.POST)

    	if form.is_valid():
    		comment = form.save(commit=False)
    		comment.post = post
    		comment.save()

    		return redirect('post_detail', post_id)
    else:
    	form = CommentForm()
    context = {
        'post': post,
        'form': form,
    }
        

    return render(request, 'blog/post_detail.html', context)


def add_post(request):
    """ Add A post to the blog """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.author = profile
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('add_post'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_post(request, post_id):
    """ Edit a post in the Blog """
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(instance=post)

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def delete_post(request, post_id):
    """ Delete a product from the store """
    post =  get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))


#def delete_comment(request, comment_id):
#    """ Delete a product from the store """
#    comment =  get_object_or_404(Comment, pk=comment_id)
#    comment.delete()
#    messages.success(request, 'Comment deleted!')
#    return redirect(reverse('post_detail', post_id))





	




		






