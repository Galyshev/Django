from django.urls import path
from users import views

urlpatterns = [
    path('authorization', views.authorization, name='authorization'),
    path('register', views.register, name='register'),
    path('logaut', views.logaut, name='logaut'),
    path('add_shop', views.add_shop, name='add_shop'),
    path('invite', views.invite, name='invite'),
    path('remove_user', views.remove_user, name='remove_user'),
    path('add_item', views.add_item, name='add_item'),
    path('analytics', views.analytics, name='analytics'),
]