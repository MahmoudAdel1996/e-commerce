from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.register, name='register'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('404/', views.error_page, name='error_page'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('<category>/', views.single_category, name='single_category'),
]