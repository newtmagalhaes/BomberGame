from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request:HttpRequest) -> HttpResponse:
  return render(request, 'game/index.html')


def bomber(request:HttpRequest) -> HttpResponse:
  return HttpResponse('Hello *bombastic* world!')
