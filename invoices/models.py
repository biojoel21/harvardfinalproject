from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(Group, blank=True, related_name="customuser_set")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="customuser_set")

class Client(models.Model):
    clientname = models.CharField(max_length=100)
    clientidnumber = models.CharField(max_length=15)
    clientemail = models.EmailField(max_length=100)
    clientphone = models.CharField(max_length=15)
    clientstate = models.CharField(max_length=2)
    clientzip = models.CharField(max_length=10)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.clientname

class Supplier(models.Model):
    suppliername = models.CharField(max_length=100)
    supplieridnumber = models.CharField(max_length=15)
    supplieremail = models.EmailField(max_length=100)
    supplierphone = models.CharField(max_length=15)
    supplierstate = models.CharField(max_length=2)
    supplierzip = models.CharField(max_length=10)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.suppliername
    
class InvoiceType(models.Model):
    invoicetype = models.CharField(max_length=100)
    
    def __str__(self):
        return self.invoicetype
    
class Invoice(models.Model):
    invoicenumber = models.CharField(max_length=100)
    invoicedate = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    invoicetype = models.ForeignKey(InvoiceType, on_delete=models.CASCADE)
    invoicetotal = models.DecimalField(max_digits=10, decimal_places=2)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.invoicenumber
   
