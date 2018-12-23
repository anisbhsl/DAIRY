from datetime import date
from bikram import samwat

##send BS date to base template
def sendBS(request):
    bs_date=samwat.from_ad(date.today())
    return {
        'bs_date':bs_date
    }

