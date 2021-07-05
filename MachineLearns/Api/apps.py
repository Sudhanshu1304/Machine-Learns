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
    global x_test,y_test
    x_test,y_test= tf.keras.datasets.mnist.load_data()[-1]
    print("Err2")
    name = 'Autoencoder'
    
    def loadModel(name):
        print("Nme : ",name)
        model = tf.keras.models.load_model("Api\\Models\\"+name)
        
        model_bottelneck = tf.keras.models.load_model("Api\\Models\\"+name+"enco")
        pred = model_bottelneck.predict(x_test)

        return [model,[pred,y_test]]
  
    def get_img():
       
        global x_test
        ind = random.randint(0,len(x_test)-1)
      
        return x_test[ind]      
