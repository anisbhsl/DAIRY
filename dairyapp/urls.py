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
    path('operationcost/',views.operationCost,name='operation-cost'),
    path('operationcost/<id>/delete',views.deleteOperationCost,name='delete-operation-cost'),
    path('report/', views.report, name='report'),
    path('report/purchasereport/',views.purchaseReport,name='purchase-report'),
    path('report/stockreport/',views.stockReport,name='stock-report'),
    path('report/salesreport/',views.salesReport,name='sales-report'),
    path('report/operationcostreport',views.operationCostReport,name='operationcost-report'),
    path('settings/',views.settings,name='settings'),
    path('settings/createproduct',views.newProductCreateView.as_view(), name='create-product'),
    path('settings/createproductunit',views.newProductUnitCreate, name='create-product-unit'),
    path('test/',views.test,name='test'),
    #path('stockrecords/<id>/delete',views.mStockRecordDelete,name='delete-stock-records'),

]