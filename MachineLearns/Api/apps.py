from django.apps import AppConfig
import tensorflow as tf
from django.contrib.staticfiles import finders


from mlxtend.data import loadlocal_mnist
import random
import numpy as np





try:
    test_images_filepath = 'images/digitimg.idx3-ubyte'
   
    test_labels_filepath = 'images/digitlab.idx1-ubyte'
    
    test_images_filepath2 = 'images/t10k-images-idx3-ubyte'
    
    test_labels_filepath2 = 'images/t10k-labels-idx1-ubyte'
    
    
    x_test3,y_test3 =  loadlocal_mnist(test_images_filepath, test_labels_filepath)
    
    x_test4,y_test4 = loadlocal_mnist(test_images_filepath2, test_labels_filepath2)
    
except:
    print(">>>>>> Err in 1")
    test_images_filepath = str(finders.find('images/digitimg.idx3-ubyte'))
    test_labels_filepath = str(finders.find('images/digitlab.idx1-ubyte'))
    test_images_filepath2 = str(finders.find('images/t10k-images-idx3-ubyte'))
    test_labels_filepath2 = str(finders.find('images/t10k-labels-idx1-ubyte'))
    x_test3,y_test3 =  loadlocal_mnist(test_images_filepath, test_labels_filepath)
    
    x_test4,y_test4 = loadlocal_mnist(test_images_filepath2, test_labels_filepath2)





x_test3 = (x_test3/255.0)[:100]
x_test3 = x_test3.reshape((len(x_test3),28,28))
y_test3 = y_test3[:100]


x_test4 = (x_test4/255.0)[:100]
x_test4 = x_test4.reshape((len(x_test4),28,28))
y_test4 = y_test4[:100]
#print("Size 22: ",len(x_test4),len(y_test4),x_test4[0].shape,x_test4.shape)
x_test = x_test3
y_test = y_test3

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'


class AutoencoderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api2'
   # print("Err1")
    global x_test,y_test
    # x_test,y_test= tf.keras.datasets.fashion_mnist.load_data()[0]
    # x_test = (x_test/255.0)[:1000]
    # y_test = y_test[:1000]
    
    
    
    #print("Err2")
    name = 'Autoencoder'
    
    def loadModel(name,name2):
        p = str(finders.find('Models/{}'.format(name)))
        model = tf.keras.models.load_model(p)
       # print("PPP : ",p)
        path22 = str(finders.find('{}enco'.format(p)))#"Api\\Models\\"+name+"enco"
       # print("Nme : ",path22)
        #path22 = 'Api/Models/abcde'
        model_bottelneck = tf.keras.models.load_model(path22)
        #print("Nmae 2 : ",len(x_test))
        pred = model_bottelneck.predict(x_test)
       # print("><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>.Pred : ",pred.shape)
        
        if name2 == 'CNN':
            return [model,[pred[:,0,0,:],y_test],model_bottelneck]
        else:
            return [model,[pred,y_test],model_bottelneck]
        
        
    def get_img(opt,noice = 'False'):
        
        global x_test,y_test
        if opt == 'Digit':
            x_test = x_test3
            y_test = y_test3
        else:
            x_test = x_test4
            y_test = y_test4
        
        ind = random.randint(0,len(x_test)-1)

        if noice == 'False':
            return x_test[ind] 
        else:
            noise_factor = 0.2

         
            #x_test = x_test + noise_factor * np.random.normal(loc = 0., scale = 1., size = x_test.shape)
            return x_test[ind]  + noise_factor * np.random.normal(loc = 0., scale = 1., size = x_test[ind].shape)
    
    
