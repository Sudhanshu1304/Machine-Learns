print("View firest")
import json
from .apps import AutoencoderConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from . import AIbackend as ai

noiceimg = None
noiceimg_j = None
digitimg = None
digitimg_j = None

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
    
    def get(self,request):
        #global IMAGE2,img2
        global noiceimg,digitimg
        print("Api Called")
        if request.method == 'GET':
            
            obj = request.GET.get('name')
 
            
            dict_obj = json.loads(obj)
         
            name = dict_obj['name']
            n_name = name.split('_')[0]
            size = int(dict_obj['size'])
            page = dict_obj['page']
            
            
            
            if page == 'digit':
                IMAGE2 = digitimg_j
                img2 = digitimg
            else:
                IMAGE2 = noiceimg_j
                img2 = noiceimg
     
            org = IMAGE2
            
            
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

            pred = {"img":json_str,"rep_img":rep_str,"org":org,"bot":bot}
        
        print(">>>>>>>>>>Clear here<<<<<<<<<<<<<< : \n")
    
        return JsonResponse(pred)



class getImage(apiView):
    
    def get(self, request):
        global noiceimg,digitimg,noiceimg_j,digitimg_j
        print("\nCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        if request.method == 'GET':
            obj = request.GET.get('opt')
            dict_obj = json.loads(obj)
            opt = dict_obj['opt']
            noice = dict_obj['noice']
           
            print("??????????????   Option |||||||||||||||||||| : ",opt,noice)
            IMAGE = AutoencoderConfig.get_img(opt,noice=noice)
            print("Shpeeeeee : ",IMAGE.shape)
            lists2 = IMAGE.reshape((IMAGE.shape[0],IMAGE.shape[1],1)).tolist()
            lists2 = ai.make_img(lists2)
            img2 = IMAGE
           
            
            org = json.dumps(lists2)
            IMAGE2 = org

            if noice=='True':
                noiceimg = img2
                noiceimg_j = IMAGE2
            else:
                digitimg = img2
                digitimg_j = IMAGE2

            pred = {"org":org}
            
        return JsonResponse(pred)