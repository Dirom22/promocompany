from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
	return render(response, "main/index.html")

def reg_cia(response):
	return render(response, "main/reg_cia.html")

data = {'name': 'Prizma'}
def company(response):
	return render(response, "main/company.html", data)

def statistics(response):
	return render(response, "main/statistics.html")