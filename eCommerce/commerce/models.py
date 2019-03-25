from django.db import models
from datetime import datetime
# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name + " | " + self.gender + " | " + self.country + " | " + self.phone


class Products(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(default="no description")
    price = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    sold_times = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class Invoices(models.Model):
    invoice_num = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    customer = models.ForeignKey('Users', on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = "Invoices"

    def __str__(self):
        return self.status + " | " + str(self.date_time.strftime('%Y-%m-%d %I:%M %p'))


class Cart(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cart"

    def __str__(self):
        return self.user.name + " => " + self.product.name