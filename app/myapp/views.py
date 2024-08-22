from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Product
from . forms import MyForm
from . models import MyModel
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})

def new(render):
    return HttpResponse('New products are coming soon')

def my_form_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MyForm()
    return render(request,'my_form_template.html', {'form':form})

def success_view(request):
    return render(request,'success_template.html')

def report_view(request):
    data = MyModel.objects.all()
    return render(request, 'report_template.html',{'data': data})