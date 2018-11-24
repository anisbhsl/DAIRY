## This template tag converts AD to BS

from django import template
from bikram import samwat
from django.utils import timezone

register=template.Library()

@register.simple_tag(name="bsconverter")
def get_BS(dateAD):
    bs_date = samwat.from_ad(dateAD.date())
    return bs_date

