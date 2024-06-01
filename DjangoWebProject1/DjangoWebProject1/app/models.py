"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title =  models.CharField(max_length= 100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content= models.TextField(verbose_name="Полное содержание")
    image=models.FileField(default="temp.jpeg", verbose_name="Путь к картинке")
    posted = models.DateTimeField(default= datetime.now(), db_index= True, verbose_name="Опбликована")
    def get_absolute_url(self):
        return reverse('blogpost', args=[str(self.id)])
    def __str__(self):
        return self.title
    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name= "статья блога"
        verbose_name_plural= "статьи блога"
admin.site.register(Blog)
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Пост", related_name="comments")
    text = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Комментарий от {self.author} "