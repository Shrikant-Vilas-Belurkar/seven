from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shri(r):
    return  render(r,'shri.html')