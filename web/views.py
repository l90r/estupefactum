from django.shortcuts import render
from web.models import Word, Date
from web import core
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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
    
@login_required
def submit(request):
    return render(request, 'submit.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
