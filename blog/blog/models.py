from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    name = models.CharField(max_length=70)
    public_id = models.CharField(max_length=40)
    publish_date = models.DateField('date of publish')
    content = models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.text
