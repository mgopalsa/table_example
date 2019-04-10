import django_filters as df
from .models import Person, Customer, Item, Order

class PersonListFilter(df.FilterSet):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']

class CustomerListFilter(df.FilterSet):
    name = df.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Customer
        fields = ['name']

class ItemListFilter(df.FilterSet):
    name = df.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Item
        fields = ['name']
