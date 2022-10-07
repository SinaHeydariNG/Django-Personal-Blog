from itertools import product
from xmlrpc.client import Boolean
from django.shortcuts import redirect, render , get_object_or_404 , HttpResponse
from . import models
from main.models import SiteInfo
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import CommentBlogForm
# Create your views here.



def list(request):

    if request.method == "POST":
        if request.POST['title']:
            title = request.POST['title']
            blogs = models.Blog.objects.filter(title__icontains = title)
            paginator = Paginator(blogs , 9)
            page =  request.GET.get('page')
            blogs = paginator.get_page(page)
    else:
        blogs = models.Blog.objects.all()
        paginator = Paginator(blogs , 2)
        page =  request.GET.get('page')
        blogs = paginator.get_page(page)

    categories = models.Category.objects.all().order_by('-title')
    information = SiteInfo.objects.last() 
    context = {
        "categories" : categories,
        "information" : information,
        "blogs" : blogs}
    return render(request , 'blog/list.html' , context)

def detail(request , slug):
    information = SiteInfo.objects.last()  
    blog = get_object_or_404(models.Blog , slug = slug)
    add_comment = CommentBlogForm()
    if request.method == "POST":
        if request.POST['parent']:
            print("Parent has been set")
            parent_id = int(request.POST['parent'])
            parent = models.Comments.objects.get(id=parent_id)
            comment_form = CommentBlogForm(request.POST)
            if comment_form.is_valid():
                new_comment = models.Comments.objects.create(
                    user = request.user,
                    blog = blog,
                    parent = parent,
                    content = request.POST['content'],
                )
                new_comment.save()
            else:
                print(comment_form.errors)
                return comment_form
        else:            
            comment_form = CommentBlogForm(request.POST)
            if comment_form.is_valid():
                new_comment = models.Comments.objects.create(
                    blog = blog,
                    user = request.user,
                    content = request.POST['content']
                )
                new_comment.save()
            else:
                print(comment_form.errors) 
                return comment_form   
    comments = models.Comments.objects.filter(blog__slug = slug)
    blogs = models.Blog.objects.all()
    paginator = Paginator(blogs , 1)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {
        "add_comment" : add_comment,
        "comments" : comments,
        "information" : information,
        "blog" : blog,
        "blogs" : blogs}
    return render(request , 'blog/detail.html' , context)

def list_by_category(request , id):
    information = SiteInfo.objects.last()
    blogs = models.Blog.objects.filter(category__id = id)
    paginator = Paginator(blogs , 9)
    page =  request.GET.get('page')
    blogs = paginator.get_page(page)
    categories = models.Category.objects.all().order_by('-title')
    context = {
        "categories" : categories,
        "information" : information,
        "blogs" : blogs}
    return render(request , 'blog/list.html' , context)

@login_required
def likePost(request , id):

    blog = models.Blog.objects.get(id = int(id))
    slug = blog.slug
    user = request.user
    print(user.likes_set)

    if Boolean(models.Likes.objects.filter(blog = blog , user = user)) == True:
        print("You cant like this post again :)")
        return redirect("../" + slug)   
    else:
        liked_post = models.Likes.objects.create(blog = blog , user = user)
        liked_post.save()  
        return redirect("../" + slug)