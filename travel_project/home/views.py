from django.http import HttpResponse
from django.shortcuts import render
from .models import blogs, second


# Create your views here.
def blog(request):
    obj=blogs.objects.all()
    unos=second.objects.all()
    return render(request,'index.html',{'data': obj,'orm': unos})



def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact.html')


