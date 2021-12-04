from django.contrib import admin
from .models import Users, Products, Invoices, Category, Comment

admin.site.register(Category)
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Invoices)
admin.site.register(Comment)
