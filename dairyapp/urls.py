from django.urls import path, include
from . import views

app_name='dairyapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('milkpurchase/',views.milkpurchase,name='milk-purchase'),
]