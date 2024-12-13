from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    prod = Product.objects.all()
    context = {'prod':prod}
    return render(request, "index.html" , context)

def mess(request):
    if request.method=="POST":
        uname = request.POST.get("uname")
        messages = request.POST.get("message")

    my_msg=Message.objects.create(name=uname, message=messages)
    my_msg.save()
    return redirect('/')