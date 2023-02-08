from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('slist', views.slist, name='slist'),
    path('add', views.add, name='add_item'),
    path('<item_id>/buy', views.buy, name='buy_item'),
    path('<item_id>/remove', views.remove, name='remove_item'),
]