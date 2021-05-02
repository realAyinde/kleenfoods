# Generated by Django 3.2 on 2021-05-02 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Card Holder Name')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254)),
                ('number', models.PositiveBigIntegerField(verbose_name='Card Number')),
                ('expiry_date', models.DateField()),
                ('cvv', models.PositiveSmallIntegerField(verbose_name='CVV / CVV2')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Amount Available')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('pin', models.PositiveSmallIntegerField()),
                ('disabled', models.BooleanField()),
            ],
            options={
                'verbose_name': 'KleenePay Debit Card',
                'verbose_name_plural': 'KleenePay Debit Cards',
            },
        ),
    ]