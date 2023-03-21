from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    url_post = models.URLField(null=True)
    author = models.CharField(max_length=100,blank=True)


def __str__(self):
    return self.title

