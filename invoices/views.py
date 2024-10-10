import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
# Create your views here.
from .models import Invoice, Client, Supplier, User, InvoiceType
from django.core.paginator import Paginator
from django.shortcuts import redirect


# Invoices views 
def index(request):
    invoices = Invoice.objects.all().order_by("id").reverse()
     # Pagination
    paginator = Paginator(invoices, 10)
    page_number = request.GET.get("page")
    invoices_page = paginator.get_page(page_number) 
    return render(request, "invoices/index.html", {
        "invoices": invoices,
        "invoices_page": invoices_page
    })    

def create(request):
    if request.method == "POST":
        # Get form information
        invoicenumber = request.POST["invoicenumber"]
        client = request.POST["client"]
        clientData = Client.objects.get(clientname=client)

        supplier = request.POST["supplier"]
        supplierData = Supplier.objects.get(suppliername=supplier)

        invoicetype = request.POST["invoicetype"]
        invoicetypeData = InvoiceType.objects.get(invoicetype=invoicetype)
        
        amount = request.POST["invoicetotal"]
        date = request.POST["invoicedate"]
                       
        # Create new todo
        invoice = Invoice(
            invoicenumber=invoicenumber,
            client=clientData, 
            supplier=supplierData, 
            invoicetype=invoicetypeData, 
            invoicetotal=amount, 
            invoicedate=date)
        invoice.save()

        invoices = Invoice.objects.all().order_by("id").reverse()
        # Redirect user to index
        # return render(request, "invoices/index.html", {
        #     "invoices": invoices
        # })
        return redirect('index')
    else:        
        clients = Client.objects.all()
        suppliers = Supplier.objects.all()
        invoicetypes = InvoiceType.objects.all()
        return render(request, "invoices/create.html", {         
               "clients": clients,
               "suppliers": suppliers,
               "invoicetypes": invoicetypes
        })    

def edit(request, invoice_id):
    if request.method == "POST":
        # Get form information
        invoicenumber = request.POST["invoicenumber"]
        client = request.POST["client"]
        clientData = Client.objects.get(clientname=client)

        supplier = request.POST["supplier"]
        supplierData = Supplier.objects.get(suppliername=supplier)

        invoicetype = request.POST["invoicetype"]
        invoicetypeData = InvoiceType.objects.get(invoicetype=invoicetype)
        
        amount = request.POST["invoicetotal"]
        date = request.POST["invoicedate"]
                       
        # Create new todo
        invoice = Invoice(
            invoicenumber=invoicenumber,
            client=clientData, 
            supplier=supplierData, 
            invoicetype=invoicetypeData, 
            invoicetotal=amount, 
            invoicedate=date)
        invoice.save()

        invoices = Invoice.objects.all().order_by("id").reverse()
        # Redirect user to index
        return render(request, "invoices/index.html", {
            "invoices": invoices
        })
    else:        
        invoice = Invoice.objects.get(id=invoice_id)
        clients = Client.objects.all()
        suppliers = Supplier.objects.all()
        invoicetypes = InvoiceType.objects.all()
        return render(request, "invoices/edit.html", {         
               "invoice": invoice,
               "clients": clients,
               "suppliers": suppliers,
               "invoicetypes": invoicetypes
        })

# Clients views
def client(request):    
    clients = Client.objects.all().order_by("id").reverse()   
     # Pagination
    paginator = Paginator(clients, 3)
    page_number = request.GET.get("page")
    clients_page = paginator.get_page(page_number) 
    return render(request, "invoices/client.html", {    
        "clients": clients,
        "clients_page": clients_page
    })

def editclient(request, client_id):
    if request.method == "POST":        
        data = json.loads(request.body)
        client = Client.objects.get(id=client_id)
        client.clientname = data["clientname"]
        client.clientidnumber = data["clientidnumber"]
        client.clientemail = data["clientemail"]
        client.clientphone = data["clientphone"]        
        client.clientstate = data["clientstate"]
        client.clientzip = data["clientzip"]
        
        client.save()
    return JsonResponse({"message": "Client updated successfully."}, status=200)

def createclient (request):
    if request.method == "POST":
        clientname = request.POST["clientname"]
        clientidnumber = request.POST["clientidnumber"]
        clientemail = request.POST["clientemail"]
        clientphone = request.POST["clientphone"]        
        clientstate = request.POST["clientstate"]
        clientzip = request.POST["clientzip"]

        client = Client(
            clientname=clientname,
            clientidnumber=clientidnumber,
            clientemail=clientemail,
            clientphone=clientphone,            
            clientstate=clientstate,
            clientzip=clientzip
        )
        client.save()
        clients = Client.objects.all().order_by("id").reverse()
        return render(request, "invoices/client.html", {
            "clients": clients
        })        

# Suppliers views
def supplier(request):
    suppliers = Supplier.objects.all().order_by("id").reverse()
     # Pagination
    paginator = Paginator(suppliers, 3)
    page_number = request.GET.get("page")
    suppliers_page = paginator.get_page(page_number) 
    return render(request, "invoices/supplier.html", {
        "suppliers": suppliers,
        "suppliers_page": suppliers_page
    })

def editsupplier(request, supplier_id):
    if request.method == "POST":
        data = json.loads(request.body)
        supplier = Supplier.objects.get(id=supplier_id)
        supplier.suppliername = data["suppliername"]
        supplier.supplieridnumber = data["supplieridnumber"]
        supplier.supplieremail = data["supplieremail"]
        supplier.supplierphone = data["supplierphone"]        
        supplier.supplierstate = data["supplierstate"]
        supplier.supplierzip = data["supplierzip"]        
        supplier.save()
    return JsonResponse({"message": "Supplier updated successfully."}, status=200)

def createsupplier (request):
    if request.method == "POST":
        suppliername = request.POST["suppliername"]
        supplieridnumber = request.POST["supplieridnumber"]
        supplieremail = request.POST["supplieremail"]
        supplierphone = request.POST["supplierphone"]        
        supplierstate = request.POST["supplierstate"]
        supplierzip = request.POST["supplierzip"]

        supplier = Supplier(
            suppliername=suppliername,
            supplieridnumber=supplieridnumber,
            supplieremail=supplieremail,
            supplierphone=supplierphone,            
            supplierstate=supplierstate,
            supplierzip=supplierzip
        )
        supplier.save()
        suppliers = Supplier.objects.all().order_by("id").reverse()
        return render(request, "invoices/supplier.html", {
            "suppliers": suppliers
        })

# Admin views
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "invoices/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "invoices/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "invoices/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "invoices/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "invoices/register.html")

