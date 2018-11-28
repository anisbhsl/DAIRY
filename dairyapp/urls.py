from django.urls import path, include
from . import views

app_name='dairyapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('milkpurchase/',views.milkPurchase,name='milk-purchase'),
    path('addmilkproducts/',views.addMilkProducts,name='add-milk-products'),
    path('sellmilkproducts/',views.sellMilkProducts,name='sell-milk-products'),
    path('stockrecords/<id>',views.mStockDetailView,name='stock-detail'),

]