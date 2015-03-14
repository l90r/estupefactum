from django.shortcuts import render

def home(request):
    context = {'word': 'dummy'}
    return render(request, 'home.html', context)

