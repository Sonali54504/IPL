from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def royal(request):
    return HttpResponse('<h1><marquee>ROYAL CHALLENGERS BENGALURU</marquee></h1>')

def virat(request):
    return render(request,'virat.html')