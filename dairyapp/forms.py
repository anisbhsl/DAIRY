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
        label='Rate',
        help_text="The rate should be in numeric format",
    )

    class Meta:
        model=mPurchase
        fields=('seller','mPurchase_product','mPurchase_qty','mPurchase_rate',)



