from django.contrib import admin
from .models import Item, User_to_list,Shop_list,MallList

admin.site.register(Item)
admin.site.register(User_to_list)
admin.site.register(Shop_list)
admin.site.register(MallList)

