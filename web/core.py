from web.models import Word, Date
from django.utils import timezone
from django.conf import settings
from enum import Enum

class WordStatus(Enum):
    OK = 0
    DAY_NOT_SCHEDULED = 1
    NOT_ENOUGH_WORDS = 2

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
    try:
        word = Word.objects.get(selected=True, its_date=today)
    except Word.DoesNotExist:
        if check_date() == Date.WORK_DAY:
            words_left = Word.objects.filter(selected=False).order_by('?')
            if len(words_left) < settings.MINIMUM_NUMBER_WORDS:
                word = Word.objects.filter(selected=True).order_by('-its_date')[0]
                return (WordStatus.NOT_ENOUGH_WORDS, word)
            word = words_left[0]
            word.selected=True
            word.its_date = today
            word.save()
        else:
            # not a work day return latest word of the day
            word = Word.objects.filter(selected=True).order_by('-its_date')[0]
            return (WordStatus.DAY_NOT_SCHEDULED, word)
    return (WordStatus.OK, word)
