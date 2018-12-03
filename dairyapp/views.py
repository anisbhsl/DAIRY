from django.shortcuts import render
from .forms import mPurchaseForm,mStockForm,mProductSellForm
from .models import mPurchase,mProduct,mStock, mProductSell
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView


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


### stock add
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
            m.mStock_date=timezone.now()
            p=get_object_or_404(mProduct,mProduct_name=mProduct_name)
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

## Detail view for stock records
def mStockDetailView(request,id):
    model=mStock
    m=get_object_or_404(mProduct,mProduct_id=id)
    stock=mStock.objects.filter(mStock_product=m.mProduct_id).order_by('-mStock_date')
    context={
        'm':m,
        'stock':stock,
    }

    return render(request,'dairyapp/stock-details.html',context)

def sellMilkProducts(request):
    title='Sell Milk Products'
    sales=mProductSell.objects.all().order_by('-mProductSell_date')
    if request.method=='POST':
        form=mProductSellForm(request.POST)
        if form.is_valid():
            m=form.save(commit=False)
            ## gives object bound to form
            ## commit = False means it gives object that has not been saved in db yet
            milk_product = form.cleaned_data.get('milk_product')
            m.mProductSell_date=timezone.now()
            p=get_object_or_404(mProduct,mProduct_name=milk_product)
            qty=form.cleaned_data.get('mProductSell_qty')
            rate=form.cleaned_data.get('mProductSell_rate')
            m.mProductSell_amount=qty*rate
            p.mProduct_qty=p.mProduct_qty-qty  ##update stock
            m.mProductSell_qtyunit=p.mProduct_qtyunit
            p.save()
            m.save()

            return redirect('/sellmilkproducts')

    else:
        form=mProductSellForm()

    context={
        'title':title,
        'form':form,
        'sales':sales,
    }
    return render(request,'dairyapp/sell-milk-products.html',context)


