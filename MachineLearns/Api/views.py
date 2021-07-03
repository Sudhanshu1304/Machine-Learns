import re
from django.shortcuts import render
from .apps import AutoencoderConfig
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.


class apiView(APIView):
    
    def get(self,request):
        
        if request.method == 'GET':
            dict = request.GET.get('dict')
            
            

            # img = dict['img']
            # name = dict['name']
            # model = AutoencoderConfig.loadModel(name)
            print(dict)
            
            pred = "Hi"#model.predict(img.reshape(-1,28,28,1))
            
            return JsonResponse(pred)



