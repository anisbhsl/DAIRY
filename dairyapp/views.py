from django.shortcuts import render

def index(request):
    title='DAIRY'
    context={
        'title':title
    }
    return render(request,'dairyapp/index.html',context)

def milkPurchase(request):
    title='Buy Milk'
    context={
        'title':title
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


