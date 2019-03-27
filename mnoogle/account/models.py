# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.db import models
#from django.conf import settings

# Create your models here.

#class products(models.Model):
#    name = models.CharField(max_length=50)
#    stock = models.CharField(max_length=30)
#    price = models.CharField(max_length=60)
#    ratings = models.CharField(max_length=2)



 #   def __str__(self):
 #       return self.name


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     dob = models.DateField(blank=True, null=True)

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='', null=True)
    city = models.CharField(max_length=100, default='', null=True)
    website = models.URLField(max_length=100, default='', blank=True, null=True)
    phone = models.CharField(max_length=10, default='', blank=True,null=True)
    image = models.FileField(upload_to='products/profile/', blank=True, null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)


class Category(models.Model):
    number = models.PositiveIntegerField(blank=True, null= True)
    name = models.CharField(max_length=150, db_index=True, null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(default=0)
    url = models.CharField(max_length=100, default="www.exampleurl.com")

    class Meta:
        ordering = ('rating',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    number = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True, default = "1")
    name = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    slug = models.SlugField(max_length=100, db_index=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available = models.NullBooleanField(default=True, null=True)
    stock = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class Mixture(models.Model):
    name = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    slug = models.SlugField(max_length=100, db_index=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    #available = models.NullBooleanField(default=False, null=True)
    stock = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='products/mixture/', null=True)



    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
