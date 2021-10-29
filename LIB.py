import numpy
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage


def gauss_blur(k, sigma): #Kernel Gaussian Blur
	G = numpy.zeros((k, k))
	for x in range(0,k):
		for y in range(0,k):
			G[x][y] = (1 / (2 * numpy.pi * sigma**2)) * numpy.exp( - ((x**2 + y**2)/(2 * sigma**2)))
	return G

def convolucion(imagen, kernel): #Convolucion de imagen
        Is = Image.open(imagen)
        I = Is.convert('L')
        I = numpy.asarray(I)
        I = I/255.0
        def pad_with(vector, pad_width, iaxis, kwargs):
                pad_value = kwargs.get('padder', 10)
                vector[:pad_width[0]]=pad_value
                vector[-pad_width[1]:]=pad_value
        I = numpy.pad(I, 10, pad_with, padder=1)
        
        j0 = ndimage.convolve(I, kernel, mode='constant', cval=0.0)
        
        plt.figure(figsize=(15,15)) #Graficas
        plt.subplot(2,2,1)
        plt.imshow(Is)
        plt.xlabel('Input Image')

        plt.subplot(2,2,2)
        plt.imshow(j0)
        plt.xlabel('Gaussian Blur')
        
        plt.grid(False)
        plt.show()
        return

