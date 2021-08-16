from django.shortcuts import render

# Create your views here.
def dileep (request):
    return render(request,'dileep.html',context={'name':'dileep','age':23})


def mahesh (request):
    return render(request,'mahesh.html',context={'name':'mahesh','age':23})