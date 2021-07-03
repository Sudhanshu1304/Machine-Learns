from django.apps import AppConfig
#from keras.models import load_model 

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'


class AutoencoderConfig(AppConfig):
    
    name = 'Autoencoder'
    
    def loadModel(self, name):
        
        # try :
        #     model = load_model(name)
        # except:
        #     model = "error"
        model = 'as'
        return model
