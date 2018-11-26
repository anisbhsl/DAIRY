from django import forms
from .models import mProduct,mPurchase, mStock
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
