from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    excerpt = models.TextField(null=True)
    content = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')



    def __str__(self):
        return f"{self.title} | By {self.author}"