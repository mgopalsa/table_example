from django import forms
from .models import Person, Item, Customer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

class PersonListFormHelper(FormHelper):
    model = Person
    form_tag = False
    layout = Layout('first_name', 'last_name', 'user', ButtonHolder(Submit('submit', 'Filter', css_class='button white right')))

class ItemListFormHelper(FormHelper):
    model = Item
    form_tag = False
    layout = Layout('name', ButtonHolder(Submit('submit', 'Filter', css_class='button white right')))

class CustomerListFormHelper(FormHelper):
    model = Customer
    form_tag = False
    layout = Layout('name', ButtonHolder(Submit('submit', 'Filter', css_class='button white right')))
