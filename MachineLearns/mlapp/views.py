from django.shortcuts import render
from django.http import Http404, response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import requests



def home(request):
    
   
    return render(request,'home.html',{})


def encoder_size(request):
    
    if request.method == 'POST':
        
      
        
        name = request.POST.get('but')
        print("\n\n>>>>>Value of name : ",name)
        
        obj = json.dumps({'name':name})
        image = requests.get('http://127.0.0.1:8000/api/?name={}'.format(obj))
    
        print("Img found",image)
    
    return render(request,'encoder_size.html',{})