# Generated by Django 3.2 on 2021-05-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210503_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
