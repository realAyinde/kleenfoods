# Generated by Django 3.2 on 2021-05-03 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_payment_amount'),
        ('core', '0002_auto_20210503_1057'),
        ('orders', '0007_alter_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='orders.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.payment'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item'),
        ),
    ]