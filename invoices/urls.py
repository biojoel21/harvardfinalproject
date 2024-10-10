from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("client/", views.client, name="client"),
    path("supplier/", views.supplier, name="supplier"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register", views.register, name="register"),    
    path("editclient/<int:client_id>", views.editclient, name="editclient"),
    path("createclient/", views.createclient, name="createclient"),
    path("editsupplier/<int:supplier_id>", views.editsupplier, name="editsupplier"),
    path("createsupplier/", views.createsupplier, name="createsupplier"),
]