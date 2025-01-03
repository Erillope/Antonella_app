from app.common.router import Router
import app.user.controllers

urlpatterns = Router.get_routes('auth') + Router.get_routes('account') + Router.get_routes('role')