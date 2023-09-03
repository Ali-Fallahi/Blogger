from multiprocessing import context

from django.urls import reverse_lazy, reverse
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.http import HttpResponseRedirect


# Create your views here.


# show blogs
# _________________________________________________________________________________________
def index(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
    }
    return render(request, 'blog/index.html', context)


# _________________________________________________________________________________________


# details of blog
# _________________________________________________________________________________________
def details(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/details.html', context)


# class BlogDetails(DetailView):
#     model = Blog
#     template_name = 'blog/details.html'
#     context_object_name = 'blog'
# _________________________________________________________________________________________


# create blog
# _________________________________________________________________________________________
# @login_required
# def add_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('blog:index')
#     else:
#         form = BlogForm()
#     return render(request, 'blog/add_blog.html', {'form': form, })

class AddBlog(CreateView):
    model = Blog
    fields = ['image', 'title', 'slug', 'category', 'body']
    template_name = 'blog/add_blog.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# _________________________________________________________________________________________


# show by category
# _________________________________________________________________________________________
def category(request, cats):
    category_name = Category.objects.get(name=cats)
    category_blogs = Blog.objects.filter(category=category_name)
    categories = Category.objects.all()

    return render(request, 'blog/category.html',
                  {'cats': cats, 'category_blogs': category_blogs, 'categories': categories})


# _________________________________________________________________________________________


# update blog
# _________________________________________________________________________________________
def update_blog(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('blog:index')
    return render(request, 'blog/add_blog.html', {'form': form, 'blog': blog})


# _________________________________________________________________________________________


# like for blogs
# _________________________________________________________________________________________
def like_view(request, slug):
    blog = get_object_or_404(Blog, slug=request.POST.get('blog_slug'))
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
    else:
        blog.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog:details', args=[slug]))
# _________________________________________________________________________________________
