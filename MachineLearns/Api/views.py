print("View firest")
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
           
           
            model,rep = AutoencoderConfig.loadModel(name)
            
            print('Model loaded' )
            img = model.predict(img.reshape((-1,28,28,1)))[0]
            
            
            lists = img.tolist()
            json_str = json.dumps(lists)
            
            rep_img = rep[0]
            rep_lab = rep[1]
            
            lists = rep_img.tolist()
            rep_str = json.dumps(lists)
            
            lists = rep_lab.tolist()
            rep_lab_str = json.dumps(lists)

            pred = {"img":json_str,"rep_img":rep_str,"rep_lab":rep_lab_str}
        
        print(">>>>>>>>>>Clear here<<<<<<<<<<<<<<")
        return JsonResponse(pred)



