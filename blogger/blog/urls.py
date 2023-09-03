from django.urls import path
from . import views
from users import views as users

app_name = "blog"

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<str:slug>/', views.details, name='details'),
    path('add/', views.AddBlog.as_view(), name='add_blog'),
    path('update/<int:id>/', views.update_blog, name='update_blog'),
    path('category/<str:cats>/', views.category, name='category'),
    path('like/<str:slug>/', views.like_view, name='like'),
]
