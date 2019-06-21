from django import template
from ..models import Products
from copy import copy
register = template.Library()


products = copy(Products.objects.all())
@register.simple_tag
def category_products(category_id):
    pro = products.filter(category=category_id)
    return len(pro)


@register.simple_tag
def total_products():
    return len(products)