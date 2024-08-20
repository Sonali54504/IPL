from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def chennai(request):
    return HttpResponse('<h1><marquee>CHENNAI SUPER KINGS</marquee></h1>')

def dhoni(request):
    return render(request,'dhoni.html')
