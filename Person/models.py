# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.ForeignKey('auth.user')
    dob = models.DateField()

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0, unique=False)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(blank=False, max_length=120, unique=True)
    order = models.ManyToManyField(Item)
    table = models.IntegerField(blank=True)
    pub_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', null=True, blank=True)
    item = models.ForeignKey(Item, related_name='orders', null=True, blank=True)
    order_date = models.DateField(auto_now=True)
    is_cancelled = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    quantity = models.IntegerField()
