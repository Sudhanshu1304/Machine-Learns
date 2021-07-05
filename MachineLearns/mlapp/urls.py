from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name='home'),
    path("encoder/",views.encoder,name='Encoder'),
    path("encosize/",views.encoder_size,name='Encoder Size'),
]
