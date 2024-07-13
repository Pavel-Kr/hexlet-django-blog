from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request):
        artticles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': artticles
        })


class ArticleView(View):
    
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article
        })
