from django.urls import path
from .views.create_view import CreateContact
from .views.list_view import ContactList
from .views.details_view import ContactDetails
from .views.update_view import UpdateContact
from .views.delete_view import DeleteContact

urlpatterns = [
    path("create", CreateContact),
    path("list", ContactList),
    path("<str:id>", ContactDetails),
    path("update/<str:id>", UpdateContact),
    path("delete/<str:id>", DeleteContact),
]
