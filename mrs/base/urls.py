from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.loginPage,name="login_page"),
    path('home/',views.mrs_home,name="mrs_home"),
]