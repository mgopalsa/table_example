# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Person, Customer, Item, Order
from .tables import PersonTable, CustomerTable, ItemTable, OrderTable
from .filters import PersonListFilter, CustomerListFilter, ItemListFilter
from .forms import PersonListFormHelper, CustomerListFormHelper, ItemListFormHelper
from .utils import PagedFilteredTableView
import django_tables2 as tables
from django.shortcuts import render

'''
from django.shortcuts import render
from tables import PersonTable
from .models import Person
import django_tables2 as tables
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class TableView(tables.SingleTableView):
    table_class = PersonTable
    table_data = Person.objects.all()
    template_name = "Person/person_list.html"
    paginate_by = 2


def person_list(request):
#    table = PersonTable(Person.objects.all())
    person_list = Person.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(person_list, 2)
    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        persons = paginator.page(1)
    except EmptyPage:
        persons = paginator.page(paginator.num_pages)
#    table.paginate(page=request.GET.get('page', 1), per_page=2)
#    RequestConfig(request, paginate={'per_page':2}).configure(table)
    return render(request, 'Person/person_list.html', {'persons':persons})
'''

class PersonList(PagedFilteredTableView):
    model = Person
    table_class = PersonTable
    filter_class = PersonListFilter
    formhelper_class = PersonListFormHelper

class CustomerList(PagedFilteredTableView):
    model = Customer
    table_class = CustomerTable
    filter_class = CustomerListFilter
    formhelper_class = CustomerListFormHelper

class ItemList(PagedFilteredTableView):
    model = Item
    table_class = ItemTable
    filter_class = ItemListFilter
    formhelper_class = ItemListFormHelper

class OrderList(tables.SingleTableView):
    model = Order
    table_class = OrderTable


def about(request):
    return render(request, 'Person/about.html', {'title':'About'})
