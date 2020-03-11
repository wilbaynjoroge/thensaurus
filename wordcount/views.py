from django.http import HttpResponse
from django.shortcuts import render
from django import template
import operator

register = template.Library()

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for x in wordlist:
        if x in worddictionary:
            #increase
            worddictionary[x] += 1
        else:
            #create new dictionary entry
            worddictionary[x] = 1
            
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords':sortedwords})