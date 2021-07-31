from django.shortcuts import render
from .AIbackend import make_img ,plot_images_encoded_in_latent_space,neck_img,make_img2
#from AIbackend import make_img



def home(request):
    return render(request,'home.html',{})


def encoder(request):
    return render(request,"encoders.html",{})


def encoder_size(request):
    
    print("Mathod : ",request.method)
    global org

    return render(request,'encoder_size.html',{})




def encoder_noice(request):

    return render(request,'encoder_noice.html',{})

