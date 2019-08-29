from django.shortcuts import render
from .forms import productform
from .models import Product
from django.http import HttpResponse
# Create your views here.
def insert(request):
    if request.method == "POST":
        form = productform(request.POST)
        if form.is_valid():
            p1=Product(pid=form.cleaned_data['pid'],
                       pname=form.cleaned_data['pname'],
                       pcost=form.cleaned_data['pcost'],
                       pmfdt=form.cleaned_data['pmfdt'],
                       pexpdt=form.cleaned_data['pexpdt'])
            p1.save()
            return HttpResponse("data inserted suceessfully")
        else:
            form = productform()
            return render(request,'input.html',{'form':form})