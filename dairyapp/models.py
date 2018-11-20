from django.db import models
from django.utils import timezone
from dairyapp.choices import MILK_CHOICES

# Create your models here.

class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=50)
    customer_address=models.CharField(max_length=100)
    customer_contact=models.CharField(max_length=10)


    def __str__(self):
        return self.customer_name

## Milk Products
class mProduct(models.Model):
    KILOGRAM='kg.'
    LITER='ltr'
    PACKET='pkt'

    MILK_PRODUCTS_UNIT_CHOICES=(
        (KILOGRAM,'Kilogram'),
        (LITER,'Liter'),
        (PACKET,'Packet'),
    )

    mProduct_id=models.AutoField(primary_key=True)
    mProduct_name=models.CharField(max_length=50)
    #mProduct_qty=models.FloatField()
    mProduct_qtyunit=models.CharField(max_length=3,choices=MILK_PRODUCTS_UNIT_CHOICES,default=LITER)  ##unit type eg. ltr, kg, ml
    #mProduct_rate=models.FloatField()


    def __str__(self):
        return self.product_name

    def mProductUnit(self):
        return self.mProduct_qtyunit


# Feeder Product
class feederProduct(models.Model):
    feederProduct_id=models.AutoField(primary_key=True)
    feederProduct_name=models.CharField(max_length=25)
    #feederProduct_qty=models.FloatField()
    feederProduct_qtyunit=models.CharField(max_length=5)
    #feederProduct_rate=models.FloatField()

    def __str__(self):
        return self.feederProduct_name

##milk purchase
class mPurchase(models.Model):

    mPurchase_id=models.AutoField(primary_key=True)
    seller=models.CharField(max_length=50)
    ## automatically set the field to now when object is created
    mPurchase_date=models.DateTimeField(default=timezone.now)
    mPurchase_product=models.CharField(max_length=10,choices=MILK_CHOICES)
    mPurchase_qty=models.FloatField()
    mPurchase_rate=models.FloatField()

    def __str__(self):
        return self.seller

## Dairy Stock
class mStock(models.Model):
    mStock_id=models.AutoField(primary_key=True)
    mProduct=models.OneToOneField(mProduct,on_delete=models.CASCADE)
    mStock_qty=models.FloatField()

    # try to access unit using mProduct.mProduct_qtyunit
    ## not sure here if it works !!
    ## check and verify it later



## milk product sell
class mProductSell(models.Model):
    mProductSell_id = models.AutoField(primary_key=True)
    buyer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    milk_product = models.OneToOneField(mProduct, on_delete=models.CASCADE)
    ## automatically set the field to now when the object is created
    mProductSell_date=models.DateTimeField(default=timezone.now)
    mProductSell_qty=models.FloatField()
    mProductSell_rate=models.FloatField()

    def __str__(self):
        return self.buyer


## feeder purchase
## class feederPurchase(models.Model):
    ##



## feeder product sell
### class feederSell(models.Model):
    ###
