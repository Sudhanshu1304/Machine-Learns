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
        

def make_img(img):
    
    plt.switch_backend("AGG")
    img = np.array(img)
    plt.imshow(img,cmap='gray')
    graph = get_graph()
    return graph

def plot_images_encoded_in_latent_space(latent_representations,sample_labels):
    latent_representations = np.array(latent_representations)
    sample_labels = np.array(sample_labels)
    plt.switch_backend("AGG")
    
    plt.scatter(latent_representations[:, 0],
                latent_representations[:, 1],
                cmap="rainbow",
                c=sample_labels,
                alpha=0.5,
                s=2)
    plt.colorbar()
    graph = get_graph()
    return graph
    

    