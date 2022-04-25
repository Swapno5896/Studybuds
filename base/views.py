import re
from django.shortcuts import render
from django.http import HttpResponse



rooms = [
    {'id':1, 'name':'data science'},
    {'id':2, 'name':'Computer science'},
    {'id':3, 'name':'Programing language'},
]
# Create your views here.
def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request, pk):
    context = {'rooms':rooms}
    return render(request, 'base/room.html',    context = {'rooms':rooms})
