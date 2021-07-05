from django.shortcuts import render
from django.http import Http404, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests
from .AIbackend import make_img 
#from AIbackend import make_img



def home(request):
    
   
    return render(request,'home.html',{})


def encoder_size(request):
    
    if request.method == 'POST':

        name = request.POST.get('but')
 
        obj = json.dumps({'name':name})
        image = requests.get('http://127.0.0.1:8000/api/?name={}'.format(obj))
        image = image.json()
        image = image['img']
        
        img = json.loads(image)
        print("\n\n^^^^^^^^^^Img found",img,type(img))
        img = make_img(img)
        
        return render(request,'encoder_size.html',{"img":img})
    
    return render(request,'encoder_size.html',{})