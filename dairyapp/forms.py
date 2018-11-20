from django import forms
from .models import mPurchase
from dairyapp.choices import MILK_CHOICES

class mPurchaseForm(forms.ModelForm):
    """
        This form is for milk purchase
    """

    seller=forms.CharField(
       label='Seller Name',
        max_length=50,
    )

    mPurchase_product=forms.ChoiceField(
        choices=MILK_CHOICES,
        label='Milk Type',
        initial='',
        widget=forms.Select(),
        required=True
    )

    mPurchase_qty=forms.FloatField(
        label='Qty'
    )

    mPurchase_rate=forms.FloatField(
        label='Rate'
    )

    class Meta:
        model=mPurchase
        fields=('seller','mPurchase_product','mPurchase_qty','mPurchase_rate',)



