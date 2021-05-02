from django.contrib import admin
from .models import DeditCard

# Register your models here.
@admin.register(DeditCard)
class DeditCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'name', 'amount', 'disabled', 'expiry_date', 'cvv']
    list_filter = ['disabled', 'created', 'updated']
