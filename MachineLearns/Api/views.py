import json
from django.shortcuts import render
from .apps import AutoencoderConfig
from django.http import JsonResponse
from rest_framework.views import APIView

# Create your views here.
print("View1")
class apiView(APIView):
    print("View2")
    def get(self,request):
        print("Api Called")
        if request.method == 'GET':
            
            obj = request.GET.get('name')
            
            dict_obj = json.loads(obj)
            name = dict_obj['name']
            #app_obj = AutoencoderConfig.get_img()
            img = AutoencoderConfig.get_img()#app_obj.get_img()
            print("Img is ",img)
            
            model = AutoencoderConfig.loadModel(name)#app_obj.loadModel(name)#AutoencoderConfig()
            #model = Model.loadModel(name)
            print('Model loaded' )
            img = model.predict(img.reshape((-1,28,28,1)))
            
            
            lists = img.tolist()
            json_str = json.dumps(lists)

            pred = {"img":json_str}#['abc']#{"Hi":dict2}#model.predict(img.reshape(-1,28,28,1))
        #print("&&& : ",pred)
        return JsonResponse(pred)



