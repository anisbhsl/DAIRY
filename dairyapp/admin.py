from django.contrib import admin
from .models import *

# Milk Products
admin.site.register(mProductUnit)
admin.site.register(mProduct)
admin.site.register(mPurchase)
# Feeder Products
admin.site.register(feederProduct)

