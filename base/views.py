from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def home_view(request):
    request.session['visits'] =  int(request.session.get('visits', 0)) + 1
    context = {
        'visits': request.session['visits']
    }
    return render(request, 'index.html', context)
