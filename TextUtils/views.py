# this is my file
from django.http import HttpResponse
from django.shortcuts import render
import string
def index(request):
    return render(request,'index2.html')
def about(request):
    return render(request,'about.html')
def analyse(request):
    analysestring = ""
    enteredtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    upper = request.GET.get('uppercase','off')
    if removepunc=='on' and upper=='on':
        for char in enteredtext:
            if char not in string.punctuation:
                analysestring = analysestring+char.upper()
    elif removepunc=='on':
        for char in enteredtext:
            if char not in string.punctuation:
                analysestring = analysestring+char
    elif upper=='on':
        analysestring = enteredtext.upper()
    else:
        analysestring = enteredtext
    mydict = {}
    mydict['result'] = analysestring

    return render(request,'analyse.html',mydict)