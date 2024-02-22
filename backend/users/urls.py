from django.urls import path
# from .view.registration_view import CreateUser
from .view.registration_view import  UserRegistrationView
from .view.profile_view import GetUser
from .view.update_view import UpdateUser
from .view.delete_view import DeleteUser
from .view.password_view import UpdatePassword
from .view.login_view import userLogin
# from .view.registration_view

urlpatterns = [
    # path("create", CreateUser),
    path("profile/<str:id>", GetUser),
    path("update/<str:id>", UpdateUser),
    path("delete/<str:id>", DeleteUser),
    path("password-update/<str:id>", UpdatePassword),
    path("login", userLogin),
    path('create', UserRegistrationView.as_view(), name='user-register'),
]
