from django import template
from ..models import Products,Users
from copy import copy
register = template.Library()

users = copy(Users.objects.all())
products = copy(Products.objects.all())
@register.simple_tag
def category_products(category_id):
    pro = products.filter(category=category_id)
    return len(pro)


@register.simple_tag
def total_products():
    return len(products)


@register.simple_tag
def get_name_from_id(user_id):
    user_name = users.get(id=user_id)
    return user_name.name


@register.simple_tag
def get_email_from_id(user_id):
    user_name = users.get(id=user_id)
    return user_name.email