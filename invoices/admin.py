from django.contrib import admin
from .models import Invoice, Client, Supplier, InvoiceType
# Register your models here.

admin.site.register(Invoice)
admin.site.register(Client)
admin.site.register(Supplier)
admin.site.register(InvoiceType)