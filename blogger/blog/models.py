from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Blog(models.Model):
    slug = models.CharField(max_length=500, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=4000)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=False)
    image = models.ImageField(default='kiaei.jpg',
                              upload_to='blog_pictures')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:details", kwargs={"slug": self.slug})
