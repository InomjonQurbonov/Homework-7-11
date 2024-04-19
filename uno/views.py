from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from news.models import News, OurWorks


class HomePageView(TemplateView,ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'

