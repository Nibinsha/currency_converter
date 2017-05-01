from django.shortcuts import render
import requests

from django.shortcuts import render_to_response
import json
from .models import currency
from .forms import currencyForm
import urllib2


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def crncy(request):
    return render(request, 'crncy.html', {})

def result(request):
    if request.method == 'POST':
       currency_from = request.POST.get('currency_from','')
       currency_to = request.POST.get('currency_to','')
       currency_input = request.POST.get('currency_input','')
       
       yql_base_url = "https://query.yahooapis.com/v1/public/yql"
       yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+currency_from+currency_to+'")'
       yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

       yql_response = urllib2.urlopen(yql_query_url)  

       yql_json = json.loads(yql_response.read())
       us = float(currency_input) * float(yql_json['query']['results']['rate']['Rate'])
       #print currency_output
       if request.method == 'POST':
    
          form = currencyForm(request.POST)
       
          if form.is_valid():
             form.save(commit=True)
       
       
    return render(request, 'result.html', {'value':us})


       

