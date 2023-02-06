# Generated by Django 4.1.6 on 2023-02-06 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_item', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MallList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_mall', models.TextField()),
                ('list_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='User_to_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('list_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.UUIDField()),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('status', models.TextField(default='нужно купить')),
                ('buy_date', models.DateTimeField(auto_now=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sl_app.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sl_app.malllist'),
        ),
    ]
