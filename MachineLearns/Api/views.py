import json
from django.shortcuts import render
from .apps import AutoencoderConfig
from django.http import JsonResponse
from rest_framework.views import APIView


class apiView(APIView):
  
    def get(self,request):
        print("Api Called")
        if request.method == 'GET':
            
            obj = request.GET.get('name')
            
            dict_obj = json.loads(obj)
            name = dict_obj['name']
         
            img = AutoencoderConfig.get_img()
           
            
            model = AutoencoderConfig.loadModel(name)
            
            print('Model loaded' )
            img = model.predict(img.reshape((-1,28,28,1)))[0]
            
            
            lists = img.tolist()
            json_str = json.dumps(lists)

            pred = {"img":json_str}
        
        return JsonResponse(pred)



