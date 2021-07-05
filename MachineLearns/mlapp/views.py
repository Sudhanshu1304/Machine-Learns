from django.shortcuts import render
from django.http import Http404, response
from numpy.lib.type_check import imag
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

import requests
from .AIbackend import make_img ,plot_images_encoded_in_latent_space
#from AIbackend import make_img



def home(request):
    
   
    return render(request,'home.html',{})


def encoder(request):
    return render(request,"encoders.html",{})


def encoder_size(request):
    
    if request.method == 'POST':

        name = request.POST.get('but')
 
        obj = json.dumps({'name':name})
        image = requests.get('http://127.0.0.1:8000/api/?name={}'.format(obj))
        image = image.json()
        image2 = image['img']
        rep_img = image['rep_img']
        rep_lab = image['rep_lab']
        img = json.loads(image2)
        rep_img = json.loads(rep_img)
        rep_lab = json.loads(rep_lab)
        
        print("\n\n^^^^^^^^^^Img found",img,type(img))
        img = make_img(img)
        rep_img = plot_images_encoded_in_latent_space(rep_img,rep_lab)
        
        return render(request,'encoder_size.html',{"img":img,"rep_img":rep_img})
    
    return render(request,'encoder_size.html',{})

