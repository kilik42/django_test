from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1> hello world</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1> hello world</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    #return HttpResponse("<h1> hello world</h1>")


    return render(request, "about.html", {})

def social_view(request, *args, **kwargs):
    #return HttpResponse("<h1> hello world</h1>")
    return render(request, "social.html", {})

def product_create_view(request, *args, **kwargs):
    #return HttpResponse("<h1> hello world</h1>")
    return render(request, "product.html", {})
