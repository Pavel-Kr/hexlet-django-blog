from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.messages import constants as msg_level
from django.views import View

from hexlet_django_blog.article.models import Article
from .forms import ArticleForm


MESSAGE_TAGS = {
    msg_level.ERROR: 'danger'
}


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


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно добавлена')
            return redirect('articles')
        return render(request, 'articles/create.html', context={
            'form': form
        })


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', context={
            'form': form,
            'article_id': article_id
        })

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно обновлена')
            return redirect('articles')
        return render(request, 'articles/update.html', context={
            'form': form,
            'article_id': article_id
        })
        

class ArticleDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.success(request, 'Статья успешно удалена')
        else:
            messages.error(request, 'Ошибка при удалении')
        return redirect('articles')
