from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Products, Category, Users, Invoices
from django.shortcuts import HttpResponse
# Create your views here.


product_on_cart = {}
x = []


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').title()
        password = request.POST.get('password')
        if username and password:
            if Users.objects.filter(name=username, password=password):
                request.session['username'] = username
                # session['username'] = username
                return redirect('home')
            else:
                error = "The username is not a valid."
                return render(request, 'Commerce/login.html', {'error': error})
        else:
            error = "The username is not a valid."
            return render(request, 'Commerce/login.html', {'error': error})
    else:
        return render(request, 'Commerce/login.html')


def register(request):
    last = Users.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username').title()
        if Users.objects.filter(name=username):
            error = 'Username Already Exist'
            return render(request, 'Commerce/signup.html', {'error': error})
        email = request.POST.get('email')
        if Users.objects.filter(email=email):
            error = 'Email Already Exist'
            return render(request, 'Commerce/signup.html', {'error1': error})
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        age = request.POST.get('age')

        if password1 == password2:
            request.session['username'] = username
            Users(id=(last.id+1),
                  name=username,
                  email=email,
                  password=password1,
                  age=age).save()
            return redirect('home')
        else:
            error = "Password Isn't match"
            return render(request, 'Commerce/signup.html', {'error2': error})

    return render(request, 'Commerce/signup.html')


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('home')


def home(request):
    items = Products.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(items, 51)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    if 'username' in request.session:
        user_login = Users.objects.get(name=request.session['username'])
    else:
        user_login = None
    context = {
        'login': user_login,
        'products': products,
        'category': categories,
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    return render(request, 'Commerce/home.html', context=context)


def single_category(request, category):
    categories = Category.objects.all()
    catalog_name = Category.objects.get(name=category)
    items = Products.objects.filter(category=catalog_name.id)
    paginator = Paginator(items, 51)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    if 'username' in request.session:
        user_login = Users.objects.get(name=request.session['username'])
    else:
        user_login = None
    context = {
        'login': user_login,
        'products': products,
        'category': categories,
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    return render(request, 'Commerce/home.html', context=context)


def single_product(request, product_id):
    product = Products.objects.get(id=product_id)
    invoices = Invoices.objects.filter(product_id=product_id)[:10]
    if 'username' in request.session:
        user_login = Users.objects.get(name=request.session['username'])
    else:
        user_login = None
    context = {
        'login': user_login,
        'product': product,
        'invoices': invoices,
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    return render(request, 'Commerce/product.html', context=context)


def search(request):
    categories = Category.objects.all()
    search_name = request.GET.get("search")
    pro = Products.objects.all()
    items = pro.filter(name__icontains=search_name)
    paginator = Paginator(items, 51)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    if 'username' in request.session:
        user_login = Users.objects.get(name=request.session['username'])
    else:
        user_login = None
    context = {
        'login': user_login,
        'products': products,
        'category': categories,
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    return render(request, 'Commerce/home.html', context=context)


def team(request):
    if 'username' in request.session:
        user_login = Users.objects.get(name=request.session['username'])
    else:
        user_login = None
    context = {
        'login': user_login,
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    return render(request, 'Commerce/team.html', context=context)


def contact(request):
    if 'username' in request.session:
        user_login = Users.objects.get(name=request.session['username'])
    else:
        user_login = None
    context = {
        'login': user_login,
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    return render(request, 'Commerce/contact.html', context=context)


def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)

    try:
        x.extend(product_on_cart.get(request.session.get('username'), []))
    except Exception as e:
        print(e)
    x.append(product)

    y = list(x)
    product_on_cart[request.session['username']] = y
    x.clear()
    return HttpResponse(len(product_on_cart[request.session['username']]))


def cart(request):
    if 'username' in request.session:
        user_login = Users.objects.get(name=request.session['username'])
    else:
        user_login = None
    context = {
        'products': product_on_cart.get(request.session.get('username')),
        'login': user_login,
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    return render(request, 'Commerce/cart.html', context=context)


def profile(request, name):
    if 'username' in request.session:
        name = name.title()
        users = Users.objects.all()
        user_login = users.get(name=request.session['username'])
        other_user = users.filter(name=name)
        if not other_user:
            return redirect('error_page')
        other_user = users.get(name=name)
        history_of_user = Invoices.objects.filter(
            customer=other_user.id
        ).order_by('-date_time')[:10]

        if not history_of_user:
            history_of_user = None
    else:
        return redirect('login')
    context = {
        'login': user_login,
        'other_user': other_user,
        'products': history_of_user,
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    return render(request, 'Commerce/profile.html', context=context)


def account(request):
    if 'username' in request.session:
        user_login = Users.objects.get(name=request.session['username'])
    else:
        return redirect('login')
    context = {
        'login': user_login,
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    if request.method == 'POST':
        user_login.password = request.POST.get('password')
        user_login.age = request.POST.get('age')
        user_login.gender = request.POST.get('gender')
        user_login.phone = request.POST.get('phone')
        user_login.country = request.POST.get('country')
        user_login.save()
    return render(request, 'Commerce/account.html', context=context)


def error_page(request):
    return render(request, 'commerce/404.html')
