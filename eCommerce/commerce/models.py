from django.db import models
# Create your models here.


# create table name commerce_users on database
class Users(models.Model):
    # add columns to this table
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=100, null=True)

    # edit table name on admin site
    class Meta:
        verbose_name_plural = "Users"

    # show string format on admin site inside the table
    def __str__(self):
        return self.name + " | " + self.gender + " | " + self.country + " | " + self.phone


# create table name commerce_products on database
class Products(models.Model):
    # add columns to this table
    name = models.CharField(max_length=500)
    description = models.TextField(default="no description")
    price = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    sold_times = models.IntegerField(default=0)

    # edit table name on admin site
    class Meta:
        verbose_name_plural = "Products"

    # show string format on admin site inside the table
    def __str__(self):
        return self.name


# create table name commerce_category on database
class Category(models.Model):
    # add columns to this table
    name = models.CharField(max_length=128)

    # edit table name on admin site
    class Meta:
        verbose_name_plural = "Category"

    # show string format on admin site inside the table
    def __str__(self):
        return self.name


# create table name commerce_invoices on database
class Invoices(models.Model):
    # add columns to this table
    invoice_num = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    customer = models.ForeignKey('Users', on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    # edit table name on admin site
    class Meta:
        verbose_name_plural = "Invoices"

    # to calculate total price
    def total_price(self):
        return self.quantity * self.product.price

    # show string format on admin site inside the table
    def __str__(self):
        return self.status + " | " + str(self.date_time.strftime('%Y-%m-%d %I:%M %p'))
