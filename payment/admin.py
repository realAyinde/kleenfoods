from django.contrib import admin
from .models import DeditCard

# Register your models here.
@admin.register(DeditCard)
class DeditCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'name', 'balance', 'disabled', 'expiry_month', 'expiry_year', 'cvv']
    list_filter = ['disabled', 'created', 'updated']
    list_editable = ['disabled']
