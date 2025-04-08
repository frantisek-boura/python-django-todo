from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# A controller is a view in django
# To map it to a URL, it needs its own entry in urls.py
def index(request):
    return HttpResponse("Todos index.")
