from django.db import models

# Create your models here.
class DeditCard(models.Model):
    name = models.CharField(("Card Holder Name"), max_length=50)
    phone = models.CharField(("Phone Number"), max_length=50)
    email = models.EmailField(max_length=254)
    number = models.PositiveBigIntegerField(("Card Number"))
    expiry_date = models.DateField(auto_now=False, auto_now_add=False)
    cvv = models.PositiveSmallIntegerField(("CVV / CVV2"))
    amount = models.DecimalField(("Amount Available"), max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pin = models.PositiveSmallIntegerField()
    disabled = models.BooleanField()

    def save(self, *args, **kwargs):
        self.amount = round(self.amount, 2)
        super(DeditCard, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "KleenePay Debit Card"
        verbose_name_plural = "KleenePay Debit Cards"

    def __str__(self):
        return self.name