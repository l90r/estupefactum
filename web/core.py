from web.models import Word, Date
from django.utils import timezone


def check_date():
    today = timezone.now().date()
    try:
        day = Date.objects.get(date=today)
        return day.date_type
    except Date.DoesNotExist:
        if today.weekday() in (5,6):
            return Date.WEEKEND
        else:
            return Date.WORK_DAY
    
def todays_word():
    today = timezone.now().date()
#    import pdb; pdb.set_trace()
    try:
        word = Word.objects.get(selected=True, its_date=today)
    except Word.DoesNotExist:
        if check_date() == Date.WORK_DAY:
            word = Word.objects.filter(selected=False).order_by('?')[0]
            word.selected=True
            word.its_date = today
            word.save()
        else:
            # not a work day return latest word of the day
            word = Word.objects.filter(selected=True).order_by('-its_date')[0]
    return word
