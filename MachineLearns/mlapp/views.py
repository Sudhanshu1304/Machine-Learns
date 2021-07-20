from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import Http404, response
from rest_framework.response import Response
import json
import matplotlib.pyplot  as plt
import requests
from .AIbackend import make_img ,plot_images_encoded_in_latent_space,neck_img,make_img2
#from AIbackend import make_img



def home(request):
    return render(request,'home.html',{})


def encoder(request):
    return render(request,"encoders.html",{})


def encoder_size(request):
    
    print("Mathod : ",request.method)
    global org
    
    # image_org = requests.get('http://127.0.0.1:8000/api/img/')
    # image_org = image_org.json()['org']
    # org = json.loads(image_org)
    # org = make_img(org)
    # print(org)
    # if request.method == "POST":
    #     #if request.POST.get('but') != None :
        
    
    #     #elif(request.method == 'POST'):
    #     image = request.POST.get('data', None)
    #     print("Imgggg : ",image)
    #     # image = image.json()
    #     return response.JsonResponse("Hello!!")
    #     # image2 = image['img']
        
    #     # rep_img = image['rep_img']
    #     # rep_lab = image['rep_lab']
    #     # #org = image_org#image['org']
        
    #     # #org = json.loads(org)
        
        
    #     # img = json.loads(image2)
        
    #     # rep_img = json.loads(rep_img)
    #     # rep_lab = json.loads(rep_lab)
    #     # img = make_img2(img)
    #     # #org = make_img(org)
    #     # rep_img = plot_images_encoded_in_latent_space(rep_img,rep_lab)
    
    # print("\n\n\n\n>>>>>>>><<<<<<<<<<HhHSHSHWUIWHW>>>>\n\n\n")
        
    #     # d = {"img":img,"rep_img":rep_img,'orgimg':org}
    #     # return render(request,'encoder_size.html',d)
    
        
    return render(request,'encoder_size.html',{})




def encoder_noice(request):
    
    print("Mathod : ",request.method)
    global org
    if request.method == "GET":
        #if request.POST.get('but') != None :
        image_org = requests.get('http://127.0.0.1:8000/api/img/')
        image_org = image_org.json()['org']
        org = json.loads(image_org)
        org = make_img(org)
  
    
    elif request.method == 'POST':
        print("But clicked!! : ",request.POST.get)
        
        if request.POST.get('exampleRadios') != None :
            name = request.POST.get('exampleRadios')
            print("Name : ",name)
            obj = json.dumps({'name':name})
            image = requests.get('http://127.0.0.1:8000/api123/?name={}'.format(obj))
            image = image.json()
            
            image2 = image['img']
            
            rep_img = image['rep_img']
            rep_lab = image['rep_lab']
            #org = image_org#image['org']
            
            #org = json.loads(org)
           
            
            img = json.loads(image2)
            
            rep_img = json.loads(rep_img)
            rep_lab = json.loads(rep_lab)
            img = make_img2(img)
            #org = make_img(org)
            rep_img = plot_images_encoded_in_latent_space(rep_img,rep_lab)
            
            d = {"img":img,"rep_img":rep_img,'orgimg':org}
            return render(request,'encoder_size.html',d)
        
        
        
        elif(request.POST.get('but')!=None):
            name = request.POST.get('but')
            print("Name : ",name)
            obj = json.dumps({'name':name})
            image = requests.get('http://127.0.0.1:8000/api123/?name={}'.format(obj))
            image = image.json()
            image2 = image['img']
            rep_img = image['rep_img']
            rep_lab = image['rep_lab']
            org = image['org']
            org = json.loads(org)
            img = json.loads(image2)
            rep_img = json.loads(rep_img)
            rep_lab = json.loads(rep_lab)
            img = make_img2(img)
            
            org = make_img(org)
            
            #neckimg = neck_img(rep_img)
            rep_img = plot_images_encoded_in_latent_space(rep_img,rep_lab)
            
            
            d = {"img":img,"rep_img":rep_img,'orgimg':org}
            return render(request,'encoder_size.html',d)#"neckimg":neckimg,

        
        #return HTTPRedirectHandler("encoder_size.html")
        
    return render(request,'encoder_noice.html',{"orgimg":org})

