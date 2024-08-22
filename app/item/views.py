from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from core.models import Items, Category
from django.contrib import messages
from django.core.paginator import Paginator
import json

existingCategory = Category.objects.all()


@login_required(login_url='login')
def index(request):
    data = Items.objects.filter(owner = request.user)
    paginator = Paginator(data, 6)
    page_number = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_number)
    return render(
        request,
        'item/index.html',
        {'categories': existingCategory, 'values': data, 'page_obj': page_obj}
    )
    