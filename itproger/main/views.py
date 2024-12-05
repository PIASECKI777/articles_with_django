from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'title': 'MAIN PAGE',
        'values': ['Some', 'HELLO', '123'],
        'thisdict':  {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
        }
    }
    return render(request, "main/index.html", data )

def about(request):
    return render(request, "main/about.html")

def contacts(request):
    return render(request, "main/contacts.html")
