from django.db import models
from django.utils import timezone
from dairyapp.choices import MILK_CHOICES
import datetime

# Create your models here.

class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=50)
    customer_address=models.CharField(max_length=100)
    customer_contact=models.CharField(max_length=10)


    def __str__(self):
        return self.customer_name


## Milk Product Units
class mProductUnit(models.Model):
    mProductUnit_id=models.AutoField(primary_key=True)
    mProductUnit_name=models.CharField(max_length=10)

    def __str__(self):
        return self.mProductUnit_name

## Milk Products
class mProduct(models.Model):
    # KILOGRAM='kg.'
    # LITER='ltr'
    # PACKET='pkt'
    #
    # MILK_PRODUCTS_UNIT_CHOICES=(
    #     (KILOGRAM,'Kilogram'),
    #     (LITER,'Liter'),
    #     (PACKET,'Packet'),
    # )

    mProduct_id=models.AutoField(primary_key=True)
    mProduct_name=models.CharField(max_length=50)
    mProduct_qtyunit = models.ForeignKey(mProductUnit,on_delete=models.CASCADE) #Product Unit has one to many relationship with mProduct
    mProduct_qty=models.FloatField(default=0) ##current stock
    #mProduct_qtyunit=models.CharField(max_length=3,choices=MILK_PRODUCTS_UNIT_CHOICES,default=LITER)  ##unit type eg. ltr, kg, ml



    def __str__(self):
        return self.mProduct_name


##milk purchase
class mPurchase(models.Model):

    mPurchase_id=models.AutoField(primary_key=True)
    seller=models.CharField(max_length=50)
    mPurchase_date=models.DateField(blank=True,null=True)
    mPurchase_product=models.CharField(max_length=15,choices=MILK_CHOICES)
    mPurchase_qty=models.FloatField()
    mPurchase_rate=models.FloatField()
    mPurchase_total=models.FloatField(default=0)

    def __str__(self):
        return self.seller

## Dairy Stock Add
class mStock(models.Model):
    mStock_id=models.AutoField(primary_key=True)
    mStock_date=models.DateTimeField(default=timezone.now)
    mStock_product=models.ForeignKey(mProduct,on_delete=models.CASCADE)
    mStock_qty=models.FloatField()

    # try to access unit using mProduct.mProduct_qtyunit
    ## not sure here if it works !!
    ## check and verify it later



## milk product sell
class mProductSell(models.Model):
    mProductSell_id = models.AutoField(primary_key=True)

    buyer_name=models.CharField(max_length=50,default='TBD')
    milk_product = models.ForeignKey(mProduct, on_delete=models.CASCADE)
    ## automatically set the field to now when the object is created
    mProductSell_date=models.DateField(blank=True,null=True,default=datetime.date.today)
    mProductSell_qty=models.FloatField()
    mProductSell_qtyunit=models.CharField(max_length=10,default='TBD')
    mProductSell_rate=models.FloatField()
    mProductSell_amount=models.FloatField(default=0)

    def __str__(self):
        return self.buyer_name


class operationCost(models.Model):
    operationCost_id=models.AutoField(primary_key=True)
    particular=models.CharField(max_length=80)
    date=models.DateField(blank=True,null=True,default=datetime.date.today)
    qty=models.FloatField()
    rate=models.FloatField()
    amount=models.FloatField()

    def __str__(self):
        return self.particular


class test(models.Model):
    test_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name