from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to later display all the list of BLOGS"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a NEW blog"
    return HttpResponse(response)

def create(request):
    response = "Placeholder to display a new form to create a NEW blog"
    return redirect('/')
def show(request, number):
    response = "placeholder to display blog " + number
    return HttpResponse(response)
def edit(request, number):
    response = "placeholder to display edit blog # " + number
    return HttpResponse(response)
def destroy(request, number):
    
    return redirect('/')

# Create your views here.
