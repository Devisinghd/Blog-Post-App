from django.db import models

# Create your models here
class Blog(models.Model):


    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True)
    published_date = models.DateTimeField()
    is_published = models.BooleanField()