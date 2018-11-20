from django.shortcuts import render
from .forms import mPurchaseForm
from .models import mPurchase
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    title='DAIRY'
    context={
        'title':title
    }
    return render(request,'dairyapp/index.html',context)

def milkPurchase(request):
    title='Buy Milk'




    if request.method=='POST':
        form=mPurchaseForm(request.POST)
        if form.is_valid():
            milk = get_object_or_404(mPurchase)
            milk=mPurchase(
                seller=form.cleaned_data.get('seller'),
                mPurchase_product=cleaned_data.get('mPurchase_product'),
                mPurchase_qty = cleaned_data.get('mPurchase_qty'),
                mPurchase_rate = cleaned_data.get('mPurchase_rate')
            )
            milk.save()

            return redirect('dairyapp/milk-purchase.html')
            

    else:
        form=mPurchaseForm()

    context = {
        'title': title,
        'form': form
    }
    return render(request,'dairyapp/milk-purchase.html',context)

def addMilkProducts(request):
    title='Add Milk Products'
    context={
        'title':title
    }
    return render(request,'dairyapp/add-milk-products.html',context)

def sellMilkProducts(request):
    title='Sell Milk Products'
    context={
        'title':title
    }
    return render(request,'dairyapp/sell-milk-products.html',context)


