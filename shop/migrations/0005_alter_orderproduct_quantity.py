# Generated by Django 4.1 on 2022-09-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_products_category_orderproduct_orderlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
