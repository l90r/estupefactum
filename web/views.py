from django.shortcuts import render
from web.models import Word, Date
from web import core

def home(request):
    try:
        word = core.todays_word()
    except:
        word = None
    context = {'word': word.content,
               'date': word.its_date,
               'work_day': core.check_date() == Date.WORK_DAY}
    return render(request, 'home.html', context)

def recent(request):
    words = Word.objects.filter(selected=True).order_by('-its_date').all()
    return render(request, 'recent.html', {'words': words})