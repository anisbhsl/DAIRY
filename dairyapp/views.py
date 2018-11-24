from django.shortcuts import render
from .forms import mPurchaseForm
from .models import mPurchase
from django.shortcuts import render, redirect
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


