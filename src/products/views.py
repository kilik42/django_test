from  django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.isValid():
        form.save()
        form = ProductForm()

    obj = Product.objects.get(id=1)
    context = {
        'object':obj
    }
    return render(request, "product/product_create.html",context)



def product_detail_view():
    obj = Product.objects.get(id=1)
    context = {
        'object':obj
    }
    return render(request, "product/detail.html",context)
