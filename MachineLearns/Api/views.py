print("View firest")
import json
from django.shortcuts import render
from .apps import AutoencoderConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from matplotlib import pyplot as plt
from . import AIbackend as ai


class apiView(APIView):
    
    def get(self,request):
        global IMAGE2,img2
        print("Api Called")
        if request.method == 'GET':
            
            obj = request.GET.get('name')
 
            
            dict_obj = json.loads(obj)
         
            name = dict_obj['name']
     
            org = IMAGE2
            
            
            model,rep = AutoencoderConfig.loadModel(name)
        
            img = model.predict(img2.reshape((-1,28,28,1)))[0]
            #img = ai.make_img(img)
            lists = img.tolist()
            lists = ai.make_img(lists)
            json_str = json.dumps(lists)
            print("6")
            rep_img = rep[0]
            rep_lab = rep[1]
            # print("7")
            # lists = rep_img.tolist()
           
            # rep_str = json.dumps(lists)
            
            # lists = rep_lab.tolist()
            # rep_lab_str = json.dumps(lists)
            
            rep_img = ai.plot_images_encoded_in_latent_space(rep_img,rep_lab)
            rep_str = json.dumps(rep_img)

            pred = {"img":json_str,"rep_img":rep_str,"org":org}
        
        print(">>>>>>>>>>Clear here<<<<<<<<<<<<<< : \n")
    
        return JsonResponse(pred)



class getImage(apiView):
    
    def get(self, request):
        global IMAGE2,img2
        print("\nCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        if request.method == 'GET':

            IMAGE = AutoencoderConfig.get_img()
            lists2 = IMAGE.reshape((IMAGE.shape[0],IMAGE.shape[1],1)).tolist()
            lists2 = ai.make_img(lists2)
            img2 = IMAGE
            
            org = json.dumps(lists2)
            IMAGE2 = org
         
            pred = {"org":org}
            
        return JsonResponse(pred)