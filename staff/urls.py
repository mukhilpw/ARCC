
from django.urls import path
from .import views

urlpatterns = [
    path('',views.vlogin,name ="nlogin"),
    path('signup/',views.vsignup,name ="nsignup"),

    path('home/',views.vhome,name="nhome"),

    path('userdata/',views.vuserdata,name="nuserdata"),
    path('userdata_form/',views.vuserdata_form,name="nuserdata_form"),

    path('hrdata/',views.vhrdata,name="nhrdata"),
    path('hrdata_form/',views.vhrdata_form,name="nhrdata_form"),

    path('accounts/',views.vaccounts,name="naccounts"),
    path('accounts_form/',views.vaccounts_form,name="naccounts_form"),

]