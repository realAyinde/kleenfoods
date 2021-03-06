# Generated by Django 3.2 on 2021-05-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='being_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
