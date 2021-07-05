import matplotlib.pyplot as plt
import time
import base64
from io import BytesIO
import random
import numpy as np



def get_graph():
    
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    img_png = buffer.getvalue()
    graph = base64.b64encode(img_png)
    graph = graph.decode('utf-8')
    buffer.close()    
    return graph
        
print("Called2!!!!")
def make_img(img):
    print("Called!!!!")
    plt.switch_backend("AGG")
    img = np.array(img)
    plt.imshow(img,cmap='gray')
    graph = get_graph()
    return graph