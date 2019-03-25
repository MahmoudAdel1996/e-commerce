from django.contrib import admin
from .models import Users, Products, Invoices

admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Invoices)
