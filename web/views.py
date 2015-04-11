from django.shortcuts import render
from django.http import Http404
from web.models import Word, Date, Page
from web import core
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from web.forms import WordSubmissionForm

def home(request):
    (status, word) = core.todays_word()
    context = {'word': word.content,
        'date': word.its_date}
    if status == core.WordStatus.NOT_ENOUGH_WORDS:
        context['alert'] = 'Not enough words. Please, submit more!'
    elif status == core.WordStatus.DAY_NOT_SCHEDULED:
        context['alert'] = 'Today is scheduled to be skipped. ' \
            'The most recent word is shown'
    return render(request, 'home.html', context)

def recent(request):
    words = Word.objects.filter(selected=True).order_by('-its_date').all()
    return render(request, 'recent.html', {'words': words})
    
def contributors(request):
    contributors = User.objects.annotate(word_count = models.Count('words')). \
                    order_by('-word_count')
    return render(request, 'contributors.html', {'contributors': contributors})
    
@login_required
def submit(request):
    if request.method == 'POST':
        form = WordSubmissionForm(request.POST)
        if(form.is_valid()):
            word = form.save(commit=False)
            word.author = request.user
            word.save()
    else:
        form = WordSubmissionForm()
    return render(request, 'submit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
def page(request, slug):
    try:
        page = Page.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request, 'static.html', {'title': page.title, 'content': page.content})
