from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.TextField(max_length=50)
    customer_address=models.TextField(max_length=50)
    customer_contact=models.IntegerField(max_length=10)


    def __str__(self):
        return self.customer_name


class Product(models.Model):