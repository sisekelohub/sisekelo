from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Post, Carousel




def post_list(request):
    posts = Post.published.all()
    return render(request,'post_list.html',{'posts':posts})


def post_detail(request, post):
    post=get_object_or_404(Post,slug=post,status='published')
    return render(request, 'post_detail.html',{'post':post})


def carousel(request):
    images = Carousel.objects.all()
    context = {
        'images':qs,
    }
    return render(request, 'base/base.html', context)


def carous(request):
    qs = Carousel.objects.all()
    # company_name = Carousel.objects.all()
    context = {
        'qs': qs,
    }
    return render( request, "base/base.html", context)

def index(request):
   
    images = Carousel.objects.all()
   
    
    context = {
       
        
        # 'candidates': user
    }
    return render(request, "base/base.html", {'images' : images,})


