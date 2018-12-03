from django.urls import path, include
from . import views

app_name='dairyapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('milkpurchase/',views.milkPurchase,name='milk-purchase'),
    path('milkpurchase/<id>/delete',views.milkPurchaseDelete,name='delete-purchase'),
    path('addmilkproducts/',views.addMilkProducts,name='add-milk-products'),
    path('sellmilkproducts/',views.sellMilkProducts,name='sell-milk-products'),
    path('sellmilkproducts/<id>/delete',views.mProductSellDelete,name='delete-sales'),
    path('stockrecords/<id>',views.mStockDetailView,name='stock-detail'),
    path('stockrecords/<id><mid>/delete',views.mStockRecordDelete,name='delete-stock-records'),


]