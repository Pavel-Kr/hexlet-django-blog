from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class index(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={
            'tag': 'python',
            'article_id': 42
        }))


def article(request, tag, article_id):
    return render(
        request,
        'articles/index.html',
        context={
            'tag': tag,
            'article_id': article_id
        }
    )
