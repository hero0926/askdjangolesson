from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mysum(request, x, y) :
	return HttpResponse(int(x)+int(y))