from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse
from .models import Products, Category
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request, 'Commerce/login.html')


def register(request):
    return render(request, 'Commerce/signup.html')


def home(request):
    items = Products.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(items, 51)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products,
        'category': categories,
    }
    return render(request, 'Commerce/home.html', context=context)


def single_category(request, category):
    categories = Category.objects.all()
    catalog_name = Category.objects.get(name=category)
    items = Products.objects.filter(category=catalog_name.id)
    paginator = Paginator(items, 51)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products,
        'category': categories,
    }
    return render(request, 'Commerce/home.html', context=context)


def search(request):
    categories = Category.objects.all()
    search_name = request.GET.get("search")
    pro = Products.objects.all()
    items = pro.filter(name__icontains=search_name)
    paginator = Paginator(items, 51)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products,
        'category': categories,
    }
    return render(request, 'Commerce/home.html', context=context)


def team(request):
    return render(request, 'Commerce/team.html')


def contact(request):
    return render(request, 'Commerce/contact.html')


def error_page(request):
    return render(request, 'commerce/404.html')