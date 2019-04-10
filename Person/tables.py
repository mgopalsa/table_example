#tables.py

import django_tables2 as tables
from .models import Person, Customer, Item, Order

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = 'django_tables2/bootstrap4.html'
        per_page = 2

class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        template_name = 'django_tables2/bootstrap4.html'
        per_page = 5

class ItemTable(tables.Table):
    class Meta:
        model = Item
        template_name = 'django_tables2/bootstrap4.html'
        per_page = 10

class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = 'django_tables2/bootstrap4.html'
        per_page = 5
