from django.shortcuts import render, redirect, get_object_or_404
from .models import Location, Comment, Post
from .forms import LocationForm, CommentModelForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment_list = Comment.objects.filter(post=post)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment_list': comment_list,
        })

def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=pk)
            comment.save()
            return redirect('blog:post_detail', pk)
    else:
        form = CommentModelForm()
    return render(request, 'blog/comment_form.html', {'form': form})


def comment_edit(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=post_id)
            comment.save()
            return redirect('blog:post_detail', post_id)
    else:
        form = CommentModelForm(instance=comment)
    return render(request, 'blog/comment_form.html', {'form': form})