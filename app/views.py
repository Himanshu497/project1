from django.shortcuts import render
from django.http import HttpResponse



def htmlfile(request):
    return render(request,'app/coffie.html')


def hai(request):
    return HttpResponse('<h1><style="color:blue"<marquee>HI HIMANSHU THIS IS FIRST DJANGO PROJECT</h1></marquee>')

def hello(request):
    return HttpResponse('<h2>THIS IS SECOND FUNCTION IN VIEWS FILE CALLED SEPERTAELY</h2>')


    
