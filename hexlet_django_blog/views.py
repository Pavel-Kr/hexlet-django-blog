from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = 'index.html'


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags}
    )


def articles(request):
    return render(request, 'articles.html')
