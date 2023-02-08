from django.urls import path
from . import views_user

urlpatterns = [
    path('authorization', views_user.authorization, name='authorization'),
    path('register', views_user.register, name='register'),
    path('add_shop', views_user.add_shop, name='add_shop'),
    path('add_item', views_user.add_item, name='add_item'),
    path('analytics', views_user.analytics, name='analytics'),
]