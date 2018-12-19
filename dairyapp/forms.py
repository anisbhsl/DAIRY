from django import forms
from .models import mProduct,mPurchase, mStock, mProductSell, operationCost,test
from dairyapp.choices import MILK_CHOICES


class mPurchaseForm(forms.ModelForm):
    """
        This form is for milk purchase
    """

    seller=forms.CharField(
       label='Seller Name',
        max_length=50,
        help_text="Please Enter Seller Name",
    )

    mPurchase_date=forms.DateTimeField(
        label='Date',
    )

    mPurchase_product=forms.ChoiceField(
        choices=MILK_CHOICES,
        label='Milk Type',
        initial='',
        widget=forms.Select(),
        help_text="Choose milk type from options",
        required=True
    )

    mPurchase_qty=forms.FloatField(
        label='Qty',
        help_text="The quantity must be in numeric format",

    )

    mPurchase_rate=forms.FloatField(
        label='Rate/Ltr',
        help_text="The rate should be in numeric format",

    )

    def __init__(self, *args, **kwargs):
        super(mPurchaseForm, self).__init__(*args, **kwargs)
        self.fields['mPurchase_date'].widget.attrs['id'] = 'nepalicalendar'

    class Meta:
        model=mPurchase
        fields=('seller','mPurchase_date','mPurchase_product','mPurchase_qty','mPurchase_rate',)

    ## Negative Value Validations
    def clean(self):
        super(mPurchaseForm,self).clean()
        mPurchase_qty = self.cleaned_data.get('mPurchase_qty')
        mPurchase_rate=self.cleaned_data.get('mPurchase_rate')

        if(mPurchase_qty<0):
            self._errors['mPurchase_qty']=self.error_class(["Negative value not allowed"])

        if(mPurchase_rate<0):
            self._errors['mPurchase_rate'] = self.error_class(["Negative value not allowed"])

        return self.cleaned_data


class mStockForm(forms.ModelForm):
    """
        This form is for adding milk product stock
    """

    mStock_product = forms.ModelChoiceField(
        queryset=mProduct.objects.filter(),
        label='Select Milk Product',
        help_text="Choose from the list of milk products",
        required=True,

    )
    mStock_date=forms.DateTimeField(
        label='Date',
        required=True,
    )
    mStock_qty = forms.FloatField(
        label='Quantity',
        help_text='Enter stock quantity',
        required=True,

    )

    def __init__(self, *args, **kwargs):
        super(mStockForm, self).__init__(*args, **kwargs)
        self.fields['mStock_date'].widget.attrs['id'] = 'nepalicalendar'


    def clean(self):
        super(mStockForm, self).clean()
        mStock_qty = self.cleaned_data.get('mStock_qty')

        ## Negative Value Validations
        if (mStock_qty < 0):
            self._errors['mStock_qty'] = self.error_class(["Negative value not allowed"])

        return self.cleaned_data

    class Meta:
        model=mStock
        fields=('mStock_product','mStock_date','mStock_qty',)





class mProductSellForm(forms.ModelForm):
    """
        This form is for selling products
    """

    buyer_name=forms.CharField(
        label='Buyer Name',
        max_length=50,
        help_text="Please Enter Buyer Name/Select From Dropdown",
        required=True,
    )

    milk_product=forms.ModelChoiceField(
        queryset=mProduct.objects.filter(),
        label='Select Milk Product',
        help_text="Choose from the list of milk products",
        required=True
    )

    mProductSell_date=forms.DateTimeField(
        label='Date',
        required=True,
    )

    mProductSell_qty = forms.FloatField(
        label='Quantity',
        help_text='Enter product quantity',
        required=True,
    )

    mProductSell_rate=forms.FloatField(
        label='Rate',
        help_text='Enter product rate',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(mProductSellForm, self).__init__(*args, **kwargs)
        self.fields['mProductSell_date'].widget.attrs['id'] = 'nepalicalendar'

    def clean(self):
        super(mProductSellForm, self).clean()
        mProductSell_qty = self.cleaned_data.get('mProductSell_qty')
        mProductSell_rate = self.cleaned_data.get('mProductSell_rate')

        ## Negative Value Validations
        if (mProductSell_qty < 0):
            self._errors['mProductSell_qty'] = self.error_class(["Negative value not allowed"])

        if (mProductSell_rate < 0):
            self._errors['mProductSell_rate'] = self.error_class(["Negative value not allowed"])

        return self.cleaned_data

    class Meta:
        model=mProductSell
        fields=('buyer_name','milk_product','mProductSell_qty', 'mProductSell_rate',)




class operationCostForm(forms.ModelForm):
    """
        This form is for operational costs!
    """

    particular=forms.CharField(
        label='Particular',
        required=True,
    )
    date=forms.CharField(
        label='Date',
        required=True,
    )

    qty=forms.FloatField(
        label='Quantity',
        help_text='Enter Quantity',
        required=True,
    )

    rate=forms.FloatField(
        label='Rate',
        help_text='Enter Rate',
        required=True,
    )

    class Meta:
        model=operationCost
        fields=('particular','date','qty','rate')

    def __init__(self, *args, **kwargs):
        super(operationCostForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['id'] = 'nepalicalendar'

    def clean(self):
        super(operationCostForm,self).clean()
        qty = self.cleaned_data.get('qty')
        rate=self.cleaned_data.get('rate')

        if(qty<0):
            self._errors['qty']=self.error_class(["Negative value not allowed"])

        if(rate<0):
            self._errors['rate'] = self.error_class(["Negative value not allowed"])

        return self.cleaned_data

class testForm(forms.ModelForm):
    name=forms.CharField(
        label='name'
    )
    date=forms.DateTimeField(
        label='date'
    )

    def __init__(self, *args, **kwargs):
        super(testForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['id'] = 'nepalicalendar'

    ## validate and clean entered date value
    def clean(self):
        super(testForm,self).clean()
        date=self.cleaned_data.get('date')



    class Meta:
        model=test
        fields=('name','date',)



