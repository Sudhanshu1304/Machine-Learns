from re import I
from django.apps import AppConfig
import tensorflow as tf
import random



class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'


class AutoencoderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api2'
    print("Err1")
    global x_test
    x_test= tf.keras.datasets.mnist.load_data()[-1][0]
    print("Err2")
    name = 'Autoencoder'
    
    def loadModel(name):
        model = tf.keras.models.load_model("Api\\Models\\"+name)
        return model
  
    def get_img():
       
        global x_test
        ind = random.randint(0,len(x_test)-1)
      
        return x_test[ind]      
