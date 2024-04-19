from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
#import requests

def dashboard(request):
    
    return render(request,'dashboard.html')