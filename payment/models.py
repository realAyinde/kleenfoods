from django.db import models
from djmoney.models.fields import MoneyField
import datetime

# Create your models here.
class DeditCard(models.Model):
    YEAR_CHOICES = [(y,y) for y in range(datetime.date.today().year, datetime.date.today().year+5)]
    MONTH_CHOICES = [(m,m) for m in range(1,13)]


    name = models.CharField(("Card Holder Name"), max_length=50)
    phone = models.CharField(("Phone Number"), max_length=50)
    email = models.EmailField(max_length=254)
    number = models.PositiveBigIntegerField(("Card Number"))
    expiry_month = models.IntegerField(choices=MONTH_CHOICES,
                  default=datetime.datetime.now().month,)
    expiry_year = models.IntegerField(choices=YEAR_CHOICES,
                 default=datetime.datetime.now().year+3,)
    cvv = models.PositiveSmallIntegerField(("CVV / CVV2"))
    balance = MoneyField(("Available Balance"), max_digits=10, decimal_places=2, default_currency='KLN')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pin = models.PositiveSmallIntegerField()
    disabled = models.BooleanField()

    class Meta:
        verbose_name = "KleenePay Debit Card"
        verbose_name_plural = "KleenePay Debit Cards"

    def __str__(self):
        return self.name

import uuid

class Payment(models.Model):
    # kleen_charge_id = models.CharField(max_length=50)
    ref_no = models.CharField(("Reference Number"), blank=True, editable=False, unique=True, max_length=36, default=uuid.uuid1)
    amount = MoneyField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)

    def __str__(self):
        return self.id
# class OrderItem(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} of {self.item.title}"

#     def get_total_item_price(self):
#         return self.quantity * self.item.price

#     def get_total_discount_item_price(self):
#         return self.quantity * self.item.discount_price

#     def get_amount_saved(self):
#         return self.get_total_item_price() - self.get_total_discount_item_price()

#     def get_final_price(self):
#         if self.item.discount_price:
#             return self.get_total_discount_item_price()
#         return self.get_total_item_price()


# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     ref_code = models.CharField(max_length=20, blank=True, null=True)
#     items = models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#     shipping_address = models.ForeignKey(
#         'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
#     billing_address = models.ForeignKey(
#         'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
#     payment = models.ForeignKey(
#         'Payment', on_delete=models.SET_NULL, blank=True, null=True)
#     coupon = models.ForeignKey(
#         'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
#     being_delivered = models.BooleanField(default=False)
#     received = models.BooleanField(default=False)
#     refund_requested = models.BooleanField(default=False)
#     refund_granted = models.BooleanField(default=False)

#     '''
#     1. Item added to cart
#     2. Adding a billing address
#     (Failed checkout)
#     3. Payment
#     (Preprocessing, processing, packaging etc.)
#     4. Being delivered
#     5. Received
#     6. Refunds
#     '''

#     def __str__(self):
#         return self.user.username

#     def get_total(self):
#         total = 0
#         for order_item in self.items.all():
#             total += order_item.get_final_price()
#         if self.coupon:
#             total -= self.coupon.amount
#         return total


# class Address(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     street_address = models.CharField(max_length=100)
#     apartment_address = models.CharField(max_length=100)
#     country = CountryField(multiple=False)
#     zip = models.CharField(max_length=100)
#     address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
#     default = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

#     class Meta:
#         verbose_name_plural = 'Addresses'


