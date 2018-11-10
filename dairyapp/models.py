from django.db import models

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
    mProduct_id=models.AutoField(primary_key=True)
    mProduct_name=models.CharField(max_length=50)
    mProduct_qty=models.FloatField()
    mProduct_qtyunit=models.CharField(max_length=5)  ##unit type eg. ltr, kg, ml
    mProduct_rate=models.FloatField()


    def __str__(self):
        return self.product_name


# Feeder Product
class feederProduct(models.Model):
    feederProduct_id=models.AutoField(primary_key=True)
    feederProduct_name=models.CharField(max_length=25)
    feederProduct_qty=models.FloatField()
    feederProduct_qtyunit=models.CharField(max_length=5)
    feederProduct_rate=models.FloatField()

    def __str__(self):
        return self.feederProduct_name

##milk purchase
## class mPurchase(models.Model):
    ####


## milk product sell
## class mProductSell(models.Model):



## feeder purchase
## class feederPurchase(models.Model):
    ##



## feeder product sell
### class feederSell(models.Model):
    ###
