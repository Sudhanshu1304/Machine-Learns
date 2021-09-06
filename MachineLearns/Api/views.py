print("View firest")
import json
from .apps import AutoencoderConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from . import AIbackend as ai
import numpy as np
import matplotlib.pyplot as plt



def pred_bottelneck(model,img,name,shape=(8,8)):
    if name == 'CNN':
        cnn = True
    else:
        cnn = False
    
   
    #img = img.reshape((img.shape[0],img.shape[1]))
    img = img.reshape(-1,img.shape[0],img.shape[1],1)
    img2 = model.predict(img)
    
    if cnn == True:
        img = img2[0,:,:,0]
    else:
        
        img = img2.reshape(shape)
    
    
    lists = img.tolist()
    lists = ai.make_img(lists)
    
    return lists   
    
    
class apiView(APIView):
    
    def post(self,request):
      
     
       
        if request.method == 'POST':
            
            dict_obj = json.load(request) # load != loads
         
            name = dict_obj['name']
            
            n_name = name.split('_')[0]
            size = int(dict_obj['size'])
            type1 = dict_obj['type'] 
            page = str(dict_obj['page'])
            Name = str(type1)+'_'+page+"_"+name
            
            img2 = dict_obj['orgimg']
            img2 = np.array(img2)
          
            
            model,rep,encod_model = AutoencoderConfig.loadModel(Name,name2=n_name)
            s = int(size**0.5)
            s2 = int(size/s)
           
            botneck = pred_bottelneck(encod_model,img2,shape=(s2,s),name=n_name)
            bot = json.dumps(botneck)
            img = model.predict(img2.reshape((-1,28,28,1)))[0]
            #img = ai.make_img(img)
            lists = img.tolist()
            lists = ai.make_img(lists)
            json_str = json.dumps(lists)
            
            rep_img = rep[0]
            rep_lab = rep[1]
    
            
            rep_img = ai.plot_images_encoded_in_latent_space(rep_img,rep_lab)
            rep_str = json.dumps(rep_img)

            pred = {"img":json_str,"rep_img":rep_str,"bot":bot}
        
           
        
            return JsonResponse(pred)



class getImage(apiView):
    
   
    def post(self, request):
      
    
        if request.method == 'POST':
            val = json.load(request)
           
           
            dict_obj = val#json.load(request)
           
            opt = dict_obj['opt']
            noice = dict_obj['noice']
           
        
            IMAGE = AutoencoderConfig.get_img(opt,noice=noice)
          
           
            lists2 = IMAGE.reshape((IMAGE.shape[0],IMAGE.shape[1],1)).tolist()
            mainimg = json.dumps(lists2)
            lists2 = ai.make_img(lists2)
           
           
            
            org = json.dumps(lists2)
        


            pred = {"org":org,'mainimg':mainimg}
            
            return JsonResponse(pred)