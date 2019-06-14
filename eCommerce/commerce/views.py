from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Products, Category, Users, Invoices
from django.shortcuts import HttpResponse
from .recommendation import recommender, recommender_2
# Create your views here.

# Create variable for cart items
product_on_cart = {}

# Create variable to copy all items on cart into it to reuse it on product_on_cart variable
x = []


# when you go to "localhost:8000/login/" login method will execute
def login(request):
    # if request is POST
    if request.method == 'POST':
        # get username from login html page and convert all words to Capitalize using title() method
        username = request.POST.get('username').title()
        # get password from login html page
        password = request.POST.get('password')
        # if username and password not null
        if username and password:
            # check if username and password already on database or not
            if Users.objects.filter(name=username, password=password):
                # set session by username for every user logged in
                request.session['username'] = username
                # go to home page "localhost:8000"
                return redirect('home')
            else:
                # if username and password isn't exist, go to login page again and show error message
                error = "The username is not a valid."
                return render(request, 'Commerce/login.html', {'error': error})
        else:
            # if username or password is null, go to login page again and show error message
            error = "The username is not a valid."
            return render(request, 'Commerce/login.html', {'error': error})
    else:
        # if method not POST, go to login page
        return render(request, 'Commerce/login.html')


# when you go to "localhost:8000/signup/" register method will execute
def register(request):
    # get last id from Users table on database
    last = Users.objects.latest('id')
    # if request method is POST
    if request.method == 'POST':
        # get username from signup html page and convert all words to Capitalize
        # using title() method like "Mahmoud Adel"
        username = request.POST.get('username').title()
        # if username already exist on database, go to signup page and show error message
        if Users.objects.filter(name=username):
            error = 'Username Already Exist'
            return render(request, 'Commerce/signup.html', {'error': error})
        # get email from signup html page
        email = request.POST.get('email')
        # if email already exist on database, go to signup page and show error message
        if Users.objects.filter(email=email):
            error = 'Email Already Exist'
            return render(request, 'Commerce/signup.html', {'error1': error})
        # get passwords from signup html page
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # get age from signup html page
        age = request.POST.get('age')
        # if passwords are equal
        if password1 == password2:
            # add username to session
            request.session['username'] = username
            # add the new user to database
            Users(id=(last.id+1),  # last.id + 1 to add new user on new id
                  name=username,
                  email=email,
                  password=password1,
                  age=age).save()
            # go to home page "localhost:8000/"
            return redirect('home')
        else:
            # if passwords aren't equal, go to signup page and show error message
            error = "Password Isn't match"
            return render(request, 'Commerce/signup.html', {'error2': error})

    # if request method isn't POST, go to signup page
    return render(request, 'Commerce/signup.html')


# when you go to "localhost:8000/logout/" logout method will execute
def logout(request):
    try:
        # remove username from session
        del request.session['username']
    except KeyError:
        pass
    # go to home page "localhost:8000/"
    return redirect('home')


# when you go to "localhost:8000/" home method will execute
def home(request):
    # get all products from database
    items = Products.objects.all()
    # get all categories from database
    categories = Category.objects.all()
    # to show only 51 product every page and show pages number
    paginator = Paginator(items, 51)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    # if user logged in
    if 'username' in request.session:
        # get this user from database to show him on upperheader html file
        user_login = Users.objects.get(name=request.session.get('username'))
    else:
        # if no user logged in
        user_login = None

    prods = list(Products.objects.all().order_by('id'))
    # if user_login:
    #     lis = recommender(user_login.id)
    # else:
    #     lis = recommender(user_login)
    lis = recommender_2()
    prolist1 = []
    for i in lis[:10]:
        prolist1.append(prods[i - 1])
    context = {
        'recommend_product': prolist1,
        'login': user_login,
        'products': products,
        'category': categories,
        # get how many products on cart if no products will return length empty list = 0
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    # go to home page "localhost:8000/"
    return render(request, 'Commerce/home.html', context=context)


# path to single category "localhost:8000/[categoryName]/"
# when you click on specific category, single_category method will execute
def single_category(request, category):
    # get all categories from database
    categories = Category.objects.all()
    # get specific category from database
    catalog_name = Category.objects.get(name=category)
    # get all products that have the category = category_name
    items = Products.objects.filter(category=catalog_name.id)
    # to show only 51 product every page and show pages number
    paginator = Paginator(items, 51)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    # if user logged in
    if 'username' in request.session:
        # get this user from database to show him on upperheader html file
        user_login = Users.objects.get(name=request.session.get('username'))
    else:
        # if no user logged in
        user_login = None

    prods = list(Products.objects.all().order_by('id'))
    # if user_login:
    #     lis = recommender(user_login.id)
    # else:
    #     lis = recommender(user_login)
    lis = recommender_2()
    prolist1 = []
    for i in lis[:10]:
        prolist1.append(prods[i - 1])
    context = {
        'recommend_product': prolist1,
        'login': user_login,
        'products': products,
        'category': categories,
        # get how many products on cart if no products will return length empty list = 0
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    # go to home page "localhost:8000/"
    return render(request, 'Commerce/home.html', context=context)


# path to single category "localhost:8000/product/[productId]/"
# when you click on specific product, single_product method will execute
def single_product(request, product_id):
    # get specific product from database
    product = Products.objects.get(id=product_id)
    # get last 10 invoices that's happened on specific product
    invoices = Invoices.objects.filter(product_id=product_id)[:10]
    # if user logged in
    if 'username' in request.session:
        # get this user from database to show him on upperheader html file
        user_login = Users.objects.get(name=request.session.get('username'))
    else:
        # if no user logged in
        user_login = None
    context = {
        'login': user_login,
        'product': product,
        'invoices': invoices,
        # get how many products on cart if no products will return length empty list = 0
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    # go to product page "localhost:8000/product/[productId]/"
    return render(request, 'Commerce/product.html', context=context)


# when you click on search icon search method will execute
def search(request):
    # get all categories from database
    categories = Category.objects.all()
    # get text from search box on html page
    search_name = request.GET.get("search")
    # get all products from database
    pro = Products.objects.all()
    # search for products that have name contain search_name text
    items = pro.filter(name__icontains=search_name)
    # to show only 51 product every page and show pages number
    paginator = Paginator(items, 51)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    # if user logged in
    if 'username' in request.session:
        # get this user from database to show him on upperheader html file
        user_login = Users.objects.get(name=request.session.get('username'))
    else:
        user_login = None

    prods = list(Products.objects.all().order_by('id'))
    # if user_login:
    #     lis = recommender(user_login.id)
    # else:
    #     lis = recommender(user_login)
    lis = recommender_2()
    prolist1 = []
    for i in lis[:10]:
        prolist1.append(prods[i - 1])

    context = {
        'recommend_product': prolist1,
        'login': user_login,
        'products': products,
        'category': categories,
        # get how many products on cart if no products will return length empty list = 0
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    # go to home page "localhost:8000/"
    return render(request, 'Commerce/home.html', context=context)


# when you go to "localhost:8000/team/" team method will execute
def team(request):
    # if user logged in
    if 'username' in request.session:
        # get this user from database to show him on upperheader html file
        user_login = Users.objects.get(name=request.session.get('username'))
    else:
        user_login = None
    context = {
        'login': user_login,
        # get how many products on cart if no products will return length empty list = 0
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    # go to team page "localhost:8000/team/"
    return render(request, 'Commerce/team.html', context=context)


# when you go to "localhost:8000/contact/" contact method will execute
def contact(request):
    # if user logged in

    if 'username' in request.session:
        # get this user from database to show him on upperheader html file
        user_login = Users.objects.get(name=request.session.get('username'))
    else:
        user_login = None
    context = {
        'login': user_login,
        # get how many products on cart if no products will return length empty list = 0
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    # go to contact page "localhost:8000/contact/"
    return render(request, 'Commerce/contact.html', context=context)


# when you click on add to cart button Ajax function call add_to_cart method
def add_to_cart(request, product_id, quantity):
    # if request method is POST
    if request.method == 'POST':
        # if user logged in
        if 'username' in request.session:
            # get the product from database you want to add
            product = Products.objects.get(id=product_id)

            try:
                # add all product from cart to list x
                x.extend(product_on_cart.get(request.session.get('username'), []))
            except Exception as e:
                print(e)
            # add the product you want to add it to list x
            x.append([product, quantity])
            # copy all products of x to y
            y = list(x)
            # add all products on y to cart
            product_on_cart[request.session.get('username')] = y
            # clear all products from list x (let x is empty)
            x.clear()
            # return to Ajax function how many products on cart to show them on html pages
            return HttpResponse(len(product_on_cart[request.session.get('username')]))
        else:
            # if user not logged in will return 'login' string to Ajax function to handel it to show alert
            return HttpResponse('login')
    else:
        # if request method not POST show error page "localhost:8000/404/"
        return redirect('error_page')


# when you click on remove from cart button Ajax function call delete_from_cart method
def delete_from_cart(request, product_id, quantity):
    # if request is DELETE
    if request.method == 'DELETE':
        # if user logged in
        if 'username' in request.session:
            # get the product from database you want to remove it from cart
            product = Products.objects.get(id=product_id)

            try:
                # add all product from cart to list x
                x.extend(product_on_cart.get(request.session.get('username'), []))
            except Exception as e:
                print(e)
            # remove the product you want to remove it from list x
            x.remove([product, quantity])
            # copy all products of x to y
            y = list(x)
            # add all products on y to cart
            product_on_cart[request.session.get('username')] = y
            # clear all products from list x (let x is empty)
            x.clear()
            # return to Ajax function how many products on cart to show them on html pages
            return HttpResponse(len(product_on_cart[request.session.get('username')]))
        else:
            # if user not logged in will return 'login' string to Ajax function to handel it to show alert
            return HttpResponse('login')
    else:
        # if request method not DELETE show error page "localhost:8000/404/"
        return redirect('error_page')


# when you go to "localhost:8000/cart/" cart method will execute or click on cart icon
def cart(request):
    # if user logged in
    if 'username' in request.session:
        # get this user from database to show him on upperheader html file
        user_login = Users.objects.get(name=request.session.get('username'))
    else:
        user_login = None
    context = {
        # get all products on cart of user_login
        'products': product_on_cart.get(request.session.get('username')),
        'login': user_login,
        # get how many products on cart if no products will return length empty list = 0
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    # go to cart page "localhost:8000/cart/"
    return render(request, 'Commerce/cart.html', context=context)


def buy_items(request):
    if request.method == 'POST':
        last = Invoices.objects.latest('invoice_num').invoice_num
        products = product_on_cart.get(request.session.get('username'))

        if products:
            for product in products:
                Invoices(
                    invoice_num=last+1,
                    customer=Users.objects.get(name=request.session.get('username')),
                    status="Buy",
                    product=product[0],
                    quantity=product[1]
                ).save()
            product_on_cart[request.session.get('username')] = []
            return HttpResponse("Successful")
        else:
            return HttpResponse("Unsuccessful")

    return redirect('error_page')


# when you go to "localhost:8000/profile/[name]"
# when you click on profile or click on name of any user
def profile(request, name):
    # if user logged in
    if 'username' in request.session:
        # convert text of name to capitalize like "Mahmoud Adel" by using title()
        name = name.title()
        # get all users from database
        users = Users.objects.all()
        # get the same user already logging in
        user_login = users.get(name=request.session.get('username'))
        # get user from database that have name = name(variable)
        other_user = users.filter(name=name)
        # if no name like this on database
        if not other_user:
            # go to error page "localhost:8000/404/"
            return redirect('error_page')
        # if found name on database then get him
        other_user = users.get(name=name)
        # get last 10 invoices of this user from database, order_by date_time
        history_of_user = Invoices.objects.filter(
            customer=other_user.id
        ).order_by('-date_time')[:10]
        # if no invoices of this user
        if not history_of_user:
            history_of_user = None
    else:
        # if user not logged in
        return redirect('login')
    context = {
        'login': user_login,
        'other_user': other_user,
        'products': history_of_user,
        # get how many products on cart if no products will return length empty list = 0
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    # go to profile page "localhost:8000/profile/[name]/"
    return render(request, 'Commerce/profile.html', context=context)


# when you click on my account button on drop menu in html page
# or when you go to "localhost:8000/account/" account method will execute
def account(request):
    # if user logged in
    if 'username' in request.session:
        # get this user from database to show him on upperheader html file
        user_login = Users.objects.get(name=request.session.get('username'))
    else:
        # go to login page "localhost:8000/login/"
        return redirect('login')
    context = {
        'login': user_login,
        # get how many products on cart if no products will return length empty list = 0
        'lenCard': len(product_on_cart.get(request.session.get('username'), []))
    }
    # if request is POST
    if request.method == 'POST':
        # edit password of the user to new password on password box on html page
        user_login.password = request.POST.get('password')
        # edit age of the user to new age on age box on html page
        user_login.age = request.POST.get('age')
        # edit gender of the user to new gender on gender box on html page
        user_login.gender = request.POST.get('gender')
        # edit phone of the user to new phone on phone box on html page
        user_login.phone = request.POST.get('phone')
        # edit country of the user to new country on country box on html page
        user_login.country = request.POST.get('country')
        # save all changes to database (commit changes)
        user_login.save()
    # go to account page "localhost:8000/account/"
    return render(request, 'Commerce/account.html', context=context)


# when you go to "localhost:8000/404/" error_page method will execute
def error_page(request):
    # go to error page "localhost:8000/404/"
    return render(request, 'commerce/404.html')
