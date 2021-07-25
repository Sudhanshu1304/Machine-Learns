from re import I
from django.apps import AppConfig
import tensorflow as tf
print('verstion :::::::::::: ',tf.__version__)
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
        
        model = tf.keras.models.load_model("Api\\Models\\"+name)
        path22 = "Api\\Models\\"+name+"enco"
        print("Nme : ",path22)
        #path22 = 'Api/Models/abcde'
        model_bottelneck = tf.keras.models.load_model(path22)
        pred = model_bottelneck.predict(x_test)
        print("><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>.Pred : ",pred.shape)
        return [model,[pred[:,0,0,:],y_test],model_bottelneck]
  
    def get_img():
       
        global x_test
        ind = random.randint(0,len(x_test)-1)
      
        return x_test[ind]   
    
    
