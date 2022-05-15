from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request:HttpRequest) -> HttpResponse:
    return render(request, 'game/index.html')


def about(request:HttpRequest) -> HttpResponse:
    return render(request, 'game/about.html')


def game(request:HttpRequest) -> HttpResponse:
    n_buttons = range(25)
    return render(request=request,
                  template_name='game/game_screen.html',
                  context={'n_buttons':n_buttons})


def rules(request:HttpRequest) -> HttpResponse:
    return render(request, 'game/rules.html')


# def bomber(request:HttpRequest) -> HttpResponse:
#     return HttpResponse('Hello *bombastic* world!')
