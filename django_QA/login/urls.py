from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login),
    path('login_page/', views.login_page),
    path('index/', views.index),
    # path('signout/', sign_in_out.signout),
    path('customers/', views.listcustomers),

]