# Generated by Django 3.2 on 2021-05-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210503_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
