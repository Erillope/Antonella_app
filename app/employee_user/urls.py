from django.urls import path
from .views import (RegisterEmployeeView, SignInView, GiveRoleView, TakeRoleView, ChangeDataView, EnableView,
                    DisableView, AddRoleView, RemoveRoleView)

urlpatterns = [
    path("auth/register", RegisterEmployeeView.as_view()),
    path("auth/signin", SignInView.as_view()),
    path("account/change_data", ChangeDataView.as_view()),
    path("account/enable", EnableView.as_view()),
    path("account/disable", DisableView.as_view()),
    path("account/give_role", GiveRoleView.as_view()),
    path("account/take_role", TakeRoleView.as_view()),
    path("role/add", AddRoleView.as_view()),
    path("role/remove", RemoveRoleView.as_view()),
]