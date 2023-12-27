from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    peoples = [
        {'name': 'John', 'age': 20},
        {'name': 'bro', 'age': 22},
        {'name': 'vikr', 'age': 24},
        {'name': 'oodod', 'age': 27},
        {'name': 'assd', 'age': 24},
    ]

    return render(request, "home/index.html", context={'peoples': peoples})

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Success Page</h1>")
