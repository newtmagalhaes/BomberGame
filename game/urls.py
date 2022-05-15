from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='sobre'),
    path('game/', views.game, name='game'),
    path('rules/', views.rules, name='regras'),
    # path('bomber/', views.bomber),
]
