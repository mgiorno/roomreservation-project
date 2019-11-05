from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html')

def login(request):
	return render(request, 'login.html')

def calendar(request):
	return render(request, 'calendar.html')

def requestform(request):
	return render(request, 'requestform.html')
