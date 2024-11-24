from django.urls import path
from .views import SignUpView, SignInView, ChangeDataView, EnableView, DisableView

urlpatterns = [
    path("auth/signup", SignUpView.as_view()),
    path("auth/signin", SignInView.as_view()),
    path("account/change_data", ChangeDataView.as_view()),
    path("account/enable", EnableView.as_view()),
    path("account/disable", DisableView.as_view()),
]