from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from .models import Post
from .forms import CommentForm

def blog(request):

    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})


# change the post detail view
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