from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def rohit(request):
    return HttpResponse('<h1><marquee>MUMBAI INDIANS</marquee></h1>')

def player(request):
    return render(request,'player.html')