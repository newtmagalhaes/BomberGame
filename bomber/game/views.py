from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def bomber(request:HttpRequest) -> HttpResponse:
  return HttpResponse('Hello *bombastic* world!')

def index(request:HttpRequest) -> HttpResponse:
  return render(request, 'index.html')