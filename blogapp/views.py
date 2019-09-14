from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .models import Portfolio

def home(request):
    blogs = Blog.objects # query set
    # 블로그의 모든 글을 대상으로
    blog_list = Blog.objects.all()
    # 블로그의 객체 네 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 2)
    # request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    # key가 page인 value를 page 변수에 담아냄
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해주기
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # query set
    return redirect('/blog/'+str(blog.id))

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})

