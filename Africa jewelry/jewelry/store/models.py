from email import message
from itertools import product
from operator import mod
from statistics import mode, quantiles
from venv import create
from django.db import models
import datetime
import os
from django.contrib.auth.models import User

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:$M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('upload/',filename)
def get_doc_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:$M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('doc/',filename)

class Category(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    status= models.BooleanField(default=False,help_text="0 = Default, 1 = Hidden" )
    trending= models.BooleanField(default=False,help_text="0 = Default, 1 = Trending " )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)
    product_image1 = models.ImageField(upload_to=get_file_path,null = False,blank = False )
    product_image2 = models.ImageField(upload_to=get_file_path,null = False,blank = False )
    product_image3 = models.ImageField(upload_to=get_file_path,null = True,blank = True )
    small_description = models.CharField(max_length=250,null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    status= models.BooleanField(default=False,help_text="0 = Default, 1 = Hidden" )
    trending= models.BooleanField(default=False,help_text="0 = Default, 1 = Trending " )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, blank=False, null=False)
    lname = models.CharField(max_length=150, blank=False, null=False)
    email = models.CharField(max_length=150, blank=False, null=False)
    phone_no = models.CharField(max_length=150, blank=False, null=False)
    street_address = models.CharField(max_length=150, blank=False, null=False)
    city = models.CharField(max_length=150, blank=False, null=False)
    order_notes = models.TextField(blank=True, null=True)
    total_price = models.FloatField(null=False)
    order_statuses ={
        ('Pending' , 'Pending'),
        ('Out for Shipping' , 'Out for Shipping'),
        ('Completed' , 'Completed')
    }
    status = models.CharField(max_length=150,choices=order_statuses,default='Pending')
    message = models.TextField(null=True)
    traking_no = models.CharField(max_length= 150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.traking_no)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.traking_no)
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50,null=False)
    street_address = models.CharField(max_length=150,null=False)
    city = models.CharField(max_length=150,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500,null=False,blank=False)
    message = models.TextField(null=False,blank=False)

    def __str__(self):
        return self.user.username

class Event(models.Model):
    title = models.CharField(max_length=300,null=False,blank=False)
    description = models.TextField(blank=False, null=False)
    image1 = models.ImageField(upload_to=get_file_path,blank=False, null=False)
    image2 = models.ImageField(upload_to=get_file_path,blank=True, null=True)
    image3 = models.ImageField(upload_to=get_file_path,blank=True, null=True)
    product = models.ForeignKey( Product,on_delete=models.CASCADE,blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    docs  = models.FileField( upload_to=get_doc_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class DiscountEvent(models.Model):
    product = models.ForeignKey( Product,on_delete=models.CASCADE,blank=False, null=False)
    title = models.CharField(max_length=300,null=False,blank=False)
    description = models.TextField(blank=False, null=False)
    expired  = models.BooleanField(default=False,help_text="0 = Default, 1 = Discount Event expired")
    created_at = models.DateTimeField(auto_now_add=True)
    ending_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title




class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username