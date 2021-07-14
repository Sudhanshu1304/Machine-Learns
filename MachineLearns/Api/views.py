print("View firest")
import json
from django.shortcuts import render
from .apps import AutoencoderConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from matplotlib import pyplot as plt


class apiView(APIView):
  
    def get(self,request):
        print("Api Called")
        if request.method == 'GET':
            
            obj = request.GET.get('name')
            
            dict_obj = json.loads(obj)
            name = dict_obj['name']
         
            img2 = AutoencoderConfig.get_img()
            
            print("Model IMG 22 SHAPE : ",img2.shape)
            lists2 = img2.reshape((img2.shape[0],img2.shape[1],1)).tolist()
            
            org = json.dumps(lists2)
            
            
            
            
            model,rep = AutoencoderConfig.loadModel(name)
            
            print('Model loaded' )
            img = model.predict(img2.reshape((-1,28,28,1)))[0]
            print("Model IMG 1 SHAPE : ",img.shape)
            lists = img.tolist()
            json_str = json.dumps(lists)
            
            rep_img = rep[0]
            rep_lab = rep[1]
            
            lists = rep_img.tolist()
            rep_str = json.dumps(lists)
            
            lists = rep_lab.tolist()
            rep_lab_str = json.dumps(lists)

            pred = {"img":json_str,"rep_img":rep_str,"rep_lab":rep_lab_str,"org":org}
        
        print(">>>>>>>>>>Clear here<<<<<<<<<<<<<<")
        return JsonResponse(pred)



