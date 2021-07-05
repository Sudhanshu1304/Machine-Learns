from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name='Home'),
    path("encosize/",views.encoder_size,name='Encoder Size'),
]
