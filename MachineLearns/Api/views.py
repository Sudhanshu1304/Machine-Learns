print("View firest")
import json
from .apps import AutoencoderConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from . import AIbackend as ai
import numpy as np




def pred_bottelneck(model,img,name,shape=(8,8)):
    if name == 'CNN':
        cnn = True
    else:
        cnn = False
        
    img = img.reshape(1,img.shape[0],img.shape[1],1)
    img2 = model.predict(img)

    if cnn == True:
        
        #img = []
        #for i in range(1):
            #I = ai.make_img(img2[0,:,:,i].tolist())
        #    img.append(I) 
        #lists = img
        img = img2[0,:,:,0]
    else:
        
        img = img2.reshape(shape)
    
    print("\n\n\nShapeeee >>>>>>> : \n\n",img.shape)
    lists = img.tolist()
    lists = ai.make_img(lists)
    print('****************************************************Pass')
    return lists   
    
    
class apiView(APIView):
    
    def post(self,request):
      
     
        print("Api Called")
        if request.method == 'POST':
            
            dict_obj = json.load(request) # load != loads
         
            name = dict_obj['name']
            n_name = name.split('_')[0]
            size = int(dict_obj['size'])
         
            
            print("Keys : ",dict_obj.keys())
            img2 = dict_obj['orgimg']
            img2 = np.array(img2)
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@   : ",img2.shape)
            
         
            
            
            model,rep,encod_model = AutoencoderConfig.loadModel(name,name2=n_name)
            s = int(size**0.5)
            s2 = int(size/s)
            print("Size >>> : ",s,s2)
            botneck = pred_bottelneck(encod_model,img2,shape=(s2,s),name=n_name)
            bot = json.dumps(botneck)
            img = model.predict(img2.reshape((-1,28,28,1)))[0]
            #img = ai.make_img(img)
            lists = img.tolist()
            lists = ai.make_img(lists)
            json_str = json.dumps(lists)
            print("6")
            rep_img = rep[0]
            rep_lab = rep[1]
    
            
            rep_img = ai.plot_images_encoded_in_latent_space(rep_img,rep_lab)
            rep_str = json.dumps(rep_img)

            pred = {"img":json_str,"rep_img":rep_str,"bot":bot}
        
            print(">>>>>>>>>>Clear here<<<<<<<<<<<<<< : \n")
        
            return JsonResponse(pred)



class getImage(apiView):
    
    print("Calleeeee : ")
    def post(self, request):
      
        print("\nCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n : ",request)
        if request.method == 'POST':
            val = json.load(request)
            print("In Her :><><><><>< \n",val)
           
            dict_obj = val#json.load(request)
            print("1 dict obj :  ",dict_obj)
            print("2 : ",dict_obj.keys())
            opt = dict_obj['opt']
            noice = dict_obj['noice']
           
        
            IMAGE = AutoencoderConfig.get_img(opt,noice=noice)
            print("Shpeeeeee : ",IMAGE.shape)
            lists2 = IMAGE.reshape((IMAGE.shape[0],IMAGE.shape[1],1)).tolist()
            mainimg = json.dumps(lists2)
            lists2 = ai.make_img(lists2)
           
           
            
            org = json.dumps(lists2)
        


            pred = {"org":org,'mainimg':mainimg}
            
            return JsonResponse(pred)