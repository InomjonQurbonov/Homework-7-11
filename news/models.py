from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    news_title = models.CharField(max_length=255)
    news_description = models.CharField(max_length=300)
    news_image = models.ImageField(upload_to='news/%Y/%m/%d', blank=True)
    news_content = models.TextField()
    news_date = models.DateTimeField(auto_now_add=True)
    news_author = models.ForeignKey(User, on_delete=models.CASCADE)
    news_views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.news_title

    class Meta:
        ordering = ['id']
        db_table = 'news'
        verbose_name = 'News'


class OurWorks(models.Model):
    work_title = models.CharField(max_length=255)
    work_description = models.CharField(max_length=300)
    work_image = models.ImageField(upload_to='works/%Y/%m/%d', blank=True)
    work_date = models.DateTimeField(auto_now_add=True)
    workers = models.CharField(max_length=255)

    def __str__(self):
        return self.work_title

    class Meta:
        ordering = ['id',]
        db_table = 'our_works'
        verbose_name = 'OurWorks'
