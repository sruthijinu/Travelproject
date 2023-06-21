from django.http import HttpResponse
from django.shortcuts import render

from travelapp.models import place, team


# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request,'index.html',{'key1':obj,'key2':obj1})

def about(request):
    return HttpResponse("am about")
def operation(request):
    a=int(request.GET['num1'])
    b=int(request.GET['num2'])
    add=a+b
    sub=a-b
    mul=a*b
    div=a//b
    return render(request,'result.html',{'key1':add,'key2':sub,'key3':mul,'key4':div})