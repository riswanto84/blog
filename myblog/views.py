from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {

    }
    return render(request, 'myblog/index.html', context)
