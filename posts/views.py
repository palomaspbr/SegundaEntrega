from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .temp_data import posts_data
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.views import generic

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

def list_posts(request):
    posts_list = Post.objects.all()
    context = {'posts_list': posts_list}
    return render(request, 'posts/index.html', context)

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        posts_list = Post.objects.filter(name__icontains=search_term)
        context = {"posts_list": posts_list}
    return render(request, 'posts/search.html', context)

def create_post(request):
    if request.method == 'POST':
        post_name = request.POST['name']
        post_description = request.POST['description']
        post_poster_url = request.POST['poster_url']
        post = Post(name=post_name,
                      description=post_description,
                      poster_url=post_poster_url)
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    else:
        return render(request, 'posts/create.html', {})
    
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.name = request.POST['name']
        post.description = request.POST['description']
        post.poster_url = request.POST['poster_url']
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'posts/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)