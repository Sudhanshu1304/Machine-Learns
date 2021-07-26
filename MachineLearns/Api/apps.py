from re import I
from django.apps import AppConfig
import tensorflow as tf
print('verstion :::::::::::: ',tf.__version__)
import random


print("clalalalalalala")


x_test3,y_test3= tf.keras.datasets.mnist.load_data()[0]
x_test3 = (x_test3/255.0)[:1000]
y_test3 = y_test3[:1000]

x_test4,y_test4= tf.keras.datasets.fashion_mnist.load_data()[0]
x_test4 = (x_test4/255.0)[:1000]
y_test4 = y_test4[:1000]

x_test = x_test3
y_test = y_test3

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'


class AutoencoderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api2'
    print("Err1")
    global x_test,y_test
    # x_test,y_test= tf.keras.datasets.fashion_mnist.load_data()[0]
    # x_test = (x_test/255.0)[:1000]
    # y_test = y_test[:1000]
    
    
    
    print("Err2")
    name = 'Autoencoder'
    
    def loadModel(name,name2):
        
        model = tf.keras.models.load_model("Api\\Models\\"+name)
        path22 = "Api\\Models\\"+name+"enco"
        print("Nme : ",path22)
        #path22 = 'Api/Models/abcde'
        model_bottelneck = tf.keras.models.load_model(path22)
        print("Nmae 2 : ",len(x_test))
        pred = model_bottelneck.predict(x_test)
        print("><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>.Pred : ",pred.shape)
        
        if name2 == 'CNN':
            return [model,[pred[:,0,0,:],y_test],model_bottelneck]
        else:
            return [model,[pred,y_test],model_bottelneck]
        
        
    def get_img(opt):
        
        global x_test,y_test
        if opt == 'digit':
            x_test = x_test3
            y_test = y_test3
        else:
            x_test = x_test4
            y_test = y_test4
        
        ind = random.randint(0,len(x_test)-1)
      
        return x_test[ind]   
    
    
