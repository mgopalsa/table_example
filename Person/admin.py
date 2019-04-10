# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person, Customer, Item, Order

admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)
