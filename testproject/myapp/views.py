from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def witaya(request):
    return HttpResponse("Witaya chaison")

def hello(request , id):
    # add hello with id to the response     
    return HttpResponse(f"Hello, {id}")

    # return HttpResponse("Witaya chaison")
def article (request ,year ,slug):
    return HttpResponse(f" This is article year is {year} and slug is {slug}")

