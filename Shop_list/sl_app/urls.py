from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('slist', views.slist, name='slist'),
    path('add_to_list', views.add_to_list, name='add_to_list'),
    path('add_ok', views.add_ok, name='add_ok'),
    path('<id>,<name_item>/buy', views.buy, name='buy'),
    path('<item_id>/remove', views.remove, name='remove_item'),
]