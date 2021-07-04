import json
from django.shortcuts import render
from .apps import AutoencoderConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.

class apiView(APIView):
    
    def get(self,request):
        print("called##################")
        if request.method == 'GET':
            dict2 = request.GET.get('data')
            
            dict2 = json.loads(dict2)
            # img = dict['img']
            # name = dict['name']
            # model = AutoencoderConfig.loadModel(name)
            print('Inside Api : ',dict2,type(dict2))
            # print('Inside Api : ',type(dict2))
            # print('Inside Api2 : ',dict(dict2))
            # print('Inside Api : ',dict(dict2['name']))
        
            pred = dict2#['abc']#{"Hi":dict2}#model.predict(img.reshape(-1,28,28,1))
        print("&&& : ",pred)
        return JsonResponse(pred)



