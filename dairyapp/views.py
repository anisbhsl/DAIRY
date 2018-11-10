from django.shortcuts import render

def index(request):
    title='DAIRY'
    context={
        'title':title
    }
    return render(request,'dairyapp/index.html',context)

def milkpurchase(request):
    title='Buy Milk'
    context={
        'title':title
    }

    return render(request,'dairyapp/milk-purchase.html',context)

