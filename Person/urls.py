from django.conf.urls import url

from . import views
#from views import TableView
urlpatterns = [
    url(r'^$', views.PersonList.as_view(), name='person_list'),
    url(r'^items/$', views.ItemList.as_view(), name='item_list'),
    url(r'^customers/$', views.CustomerList.as_view(), name='customer_list'),
    url(r'^orders/$', views.OrderList.as_view(), name='order_list'),
#    url(r'^$', views.person_list, name='person_list'),
    url(r'^about/$', views.about, name='About'),
]
