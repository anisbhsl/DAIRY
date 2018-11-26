from django.shortcuts import render
from .forms import mPurchaseForm,mStockForm
from .models import mPurchase,mProduct
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import datetime


def index(request):
    title='DAIRY'
    context={
        'title':title
    }
    return render(request,'dairyapp/index.html',context)

def milkPurchase(request):
    title='Buy Milk'
    milk = mPurchase.objects.all().order_by('-mPurchase_date')

    if request.method=='POST':
        form=mPurchaseForm(request.POST)
        if form.is_valid():
            m=form.save(commit=False)
            ## gives object bound to form
            ## commit = False means it gives object that has not been saved in db yet
            m.mPurchase_date=timezone.now()
            m.mPurchase_total=m.mPurchase_qty*m.mPurchase_rate
            m.save()
            return redirect('/milkpurchase')

    else:
        form=mPurchaseForm()

    context = {
        'title': title,
        'form': form,
        'milk': milk

    }

    return render(request,'dairyapp/milk-purchase.html',context)
def addMilkProducts(request):
    title='Add Milk Products'
    product=mProduct.objects.all().order_by('-mProduct_name')

    if request.method=='POST':
        form=mStockForm(request.POST)
        if form.is_valid():
            m=form.save(commit=False)

            ## gives object bound to form
            ## commit = False means it gives object that has not been saved in db yet
            mProduct_name=form.cleaned_data.get('mStock_product')

            p=get_object_or_404(mProduct,mProduct_name=mProduct_name)
            print(p)
            print("printing...................")
            qty=form.cleaned_data.get('mStock_qty')
            p.mProduct_qty=p.mProduct_qty+qty  ##update stock

            p.save()
            m.save()

            return redirect('/addmilkproducts')

    else:
        form=mStockForm()
    context={
        'title':title,
        'product':product,
        'form':form,
    }
    return render(request,'dairyapp/add-milk-products.html',context)

def sellMilkProducts(request):
    title='Sell Milk Products'
    context={
        'title':title
    }
    return render(request,'dairyapp/sell-milk-products.html',context)


