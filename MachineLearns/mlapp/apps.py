from django.apps import AppConfig
# from keras.datasets import mnist
# import random

class MlappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mlapp'


# (x_train,y_tarin),(x_test,y_test) = mnist.load_data()



# class GetImageConfig(AppConfig):
#     name='images'
    
#     def get_img():
        
#         ind = random.randint(0,len(x_test)-1)
#         print('iiiiiiii ccc : ',x_test[ind]  )
#         return x_test[ind]        
    
