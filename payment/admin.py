from django.contrib import admin
from .models import DeditCard, Payment

# Register your models here.
@admin.register(DeditCard)
class DeditCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'name', 'balance', 'disabled', 'expiry_month', 'expiry_year', 'cvv']
    list_filter = ['disabled', 'created', 'updated']
    list_editable = ['disabled']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['ref_no', 'amount', 'success']