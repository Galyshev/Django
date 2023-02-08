from django.db import models


class Shop_list(models.Model):
    # list_id = models.UUIDField()
    list_id = models.TextField()
    item_id = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, null=True, max_digits=20)
    status = models.TextField(default='нужно купить')
    buy_date = models.DateTimeField(auto_now=True)


class User_to_list(models.Model):
    user_id = models.IntegerField()
    # list_id = models.UUIDField()
    list_id = models.TextField()


class MallList(models.Model):
    name_mall = models.TextField()
    # list_id = models.UUIDField()
    list_id = models.TextField()
    # Так можно создать вторичный ключ на конкретную колонку
    # list_id = models.ForeignKey(Shop_list, on_delete=models.PROTECT, related_name='%(class)s_list_id')

class Item(models.Model):
    name_item = models.TextField()
    shop_id = models.ForeignKey("MallList", on_delete=models.CASCADE)
