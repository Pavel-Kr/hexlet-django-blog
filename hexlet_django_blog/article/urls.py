from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.index.as_view()),
    path('<str:tag>/<int:article_id>/', views.article, name='article')
]