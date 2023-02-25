from django.db import models


class Shop_list(models.Model):
    list_id = models.UUIDField()
    item_id = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, null=True, max_digits=20)
    status = models.TextField(default='купить')
    buy_date = models.DateTimeField(auto_now=True)


class User_to_list(models.Model):
    user_id = models.IntegerField()
    list_id = models.UUIDField()
    or_list = models.UUIDField()

class MallList(models.Model):
    name_mall = models.TextField()
    list_id = models.UUIDField()

class Item(models.Model):
    name_item = models.TextField()
    shop_id = models.ForeignKey("MallList", on_delete=models.CASCADE)
