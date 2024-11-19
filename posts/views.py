from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import posts_data
from django.http import HttpResponseRedirect
from django.urls import reverse

def detail_post(request, post_id):
    context = {'post': posts_data[post_id - 1]}
    return render(request, 'posts/detail.html', context)

def list_posts(request):
    context = {"posts_list": posts_data}
    return render(request, 'posts/index.html', context)


def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "posts_list": [
                m for m in posts_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'posts/search.html', context)

def create_post(request):
    if request.method == 'POST':
        posts_data.append({
            'name': request.POST['name'],
            'descritpion': request.POST['description'],
            'poster_url': request.POST['poster_url']
        })
        return HttpResponseRedirect(
            reverse('movies:detail', args=(len(posts_data), )))
    else:
        return render(request, 'posts/create.html', {})