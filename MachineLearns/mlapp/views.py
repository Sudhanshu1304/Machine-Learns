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
    
    print("Req : ",request)
    
    data = {"abc":1234}
    j = json.dumps(data)
    print(j)
    res = requests.get('http://127.0.0.1:8000/api/?data={}'.format(j))
    print("Req est is : ! ",res.json())
    #print('>>>>res : ',json.loads(res))
    return render(request,'home.html',{})


