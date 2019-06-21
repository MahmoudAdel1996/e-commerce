from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('profile/<name>', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('product/<product_id>/', views.single_product, name='single_product'),
    path('add_to_cart/<product_id>/<quantity>/', views.add_to_cart, name='add_cart'),
    path('delete_from_cart/<product_id>/<quantity>/', views.delete_from_cart, name='delete_cart'),
    path('cart/buy/', views.buy_items, name='buy'),
    path('404/', views.error_page, name='error_page'),
    path('search/', views.search, name='search'),
    path('category/<category>/', views.single_category, name='single_category'),
    path('recommender/', views.get_recommender, name='get_recommender'),

]