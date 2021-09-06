from django.shortcuts import render

def home(request):
    return render(request,'home.html',{})


def encoder(request):
    return render(request,"encoders.html",{})


def encoder_size(request):
    
    
    global org

    return render(request,'encoder_size.html',{})




def encoder_noice(request):

    return render(request,'encoder_noice.html',{})

def blogs(request):
    return render(request,'blogs.html',{})