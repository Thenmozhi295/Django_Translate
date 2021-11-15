from django.shortcuts import render
from django.utils.translation import gettext as _

def home(request):
    text=_("Have a good day")
    #return render(request,'home.html',{'text': text})

    return render(request, 'switchlangexample/home.html',{'text': text})
