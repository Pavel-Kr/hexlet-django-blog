from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request):
        artticles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': artticles
        })


def article(request, tag, article_id):
    return render(
        request,
        'articles/index.html',
        context={
            'tag': tag,
            'article_id': article_id
        }
    )
