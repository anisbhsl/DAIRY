from django import forms
from .models import mProduct,mPurchase, mStock, mProductSell, operationCost
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

    class Meta:
        model=mPurchase
        fields=('seller','mPurchase_product','mPurchase_qty','mPurchase_rate',)

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
    mStock_qty = forms.FloatField(
        label='Quantity',
        help_text='Enter stock quantity',

    )

    class Meta:
        model=mStock
        fields=('mStock_product','mStock_qty',)

    def clean(self):
        super(mStockForm, self).clean()
        mStock_qty = self.cleaned_data.get('mStock_qty')

        ## Negative Value Validations
        if (mStock_qty < 0):
            self._errors['mStock_qty'] = self.error_class(["Negative value not allowed"])

        return self.cleaned_data

class mProductSellForm(forms.ModelForm):
    """
        This form is for selling products
    """

    buyer_name=forms.CharField(
       label='Buyer Name',
        max_length=50,
        help_text="Please Enter Buyer Name/Select From Dropdown",
    )

    milk_product=forms.ModelChoiceField(
        queryset=mProduct.objects.filter(),
        label='Select Milk Product',
        help_text="Choose from the list of milk products",
        required=True
    )

    mProductSell_qty = forms.FloatField(
        label='Quantity',
        help_text='Enter product quantity',

    )

    mProductSell_rate=forms.FloatField(
        label='Rate',
        help_text='Enter product rate',

    )

    class Meta:
        model=mProductSell
        fields=('buyer_name','milk_product','mProductSell_qty', 'mProductSell_rate',)


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

class operationCostForm(forms.ModelForm):
    """
        This form is for operational costs!
    """

    particular=forms.CharField(
        label='Particular',

    )

    qty=forms.FloatField(
        label='Quantity',
        help_text='Enter Quantity',
    )

    rate=forms.FloatField(
        label='Rate',
        help_text='Enter Rate',
    )

    class Meta:
        model=operationCost
        fields=('particular','qty','rate')

    def clean(self):
        super(operationCostForm,self).clean()
        qty = self.cleaned_data.get('qty')
        rate=self.cleaned_data.get('rate')

        if(qty<0):
            self._errors['qty']=self.error_class(["Negative value not allowed"])

        if(rate<0):
            self._errors['rate'] = self.error_class(["Negative value not allowed"])

        return self.cleaned_data