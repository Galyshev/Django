# Generated by Django 4.1.6 on 2023-02-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sl_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malllist',
            name='list_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shop_list',
            name='list_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user_to_list',
            name='list_id',
            field=models.TextField(),
        ),
    ]
