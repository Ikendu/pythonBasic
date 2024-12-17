from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# def members(request):
#     return HttpResponse("Hello world")

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('myfirst.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('testing.html')
    context = {
        'fruits': ['Apple', 'Mango', 'Covar', 'Sugarcane']
    }
    return HttpResponse(template.render(context, request))