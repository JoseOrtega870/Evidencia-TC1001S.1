import numpy
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage


"""
Funcion Gaussian Blur por Fabian Gonzalez Vera
Recibe tamanio del kernel y valor de sigma
Regresa G
"""

def gauss_blur(k, sigma): 
	G = numpy.zeros((k, k))
	for x in range(0,k):
		for y in range(0,k):
			G[x][y] = (1 / (2 * numpy.pi * sigma**2)) * numpy.exp( - ((x**2 + y**2)/(2 * sigma**2)))
	return G

"""
Funcion Laplacian of Gaussian por Jose Ortega Guido
Recibe tamanio del kernel y valor de sigma
Regresa M
"""

def laplacianOfGaussian(sigma, K): 
    M = numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            M[x][y] = -(1/(numpy.pi*sigma**4)) * (1-((x**2+y**2)/(2*sigma**2))) \
                        * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return M

"""
Funciones de Sobel por Rodolfo de la O
Recibe el tamnio del kernel y regresan M
"""

def Sobel_Top(K): 
    M = numpy.zeros((K,K))
    M[K//2][K//2] = 0
    M[K//2 + 1][K//2] = -2
    M[K//2 - 1][K//2] = 2
    M[K//2][K//2 + 1] = 0
    M[K//2][K//2 - 1] = 0
    M[K//2 + 1][K//2 + 1] = -1
    M[K//2 + 1][K//2 - 1] = -1
    M[K//2 - 1][K//2 + 1] = 1
    M[K//2 - 1][K//2 - 1] = 1
    return M

def Sobel_right(K):
    M = numpy.zeros((K,K))
    M[K//2][K//2] = 0
    M[K//2 + 1][K//2] = 0
    M[K//2 - 1][K//2] = 0
    M[K//2][K//2 + 1] = 2
    M[K//2][K//2 - 1] = -2
    M[K//2 + 1][K//2 + 1] = 1
    M[K//2 + 1][K//2 - 1] = -1
    M[K//2 - 1][K//2 + 1] = 1
    M[K//2 - 1][K//2 - 1] = -1
    return M

def Sobel_left(K):
    M = numpy.zeros((K,K))
    M[K//2][K//2] = 0
    M[K//2 + 1][K//2] = 0
    M[K//2 - 1][K//2] = 0
    M[K//2][K//2 + 1] = -2
    M[K//2][K//2 - 1] = 2
    M[K//2 + 1][K//2 + 1] = -1
    M[K//2 + 1][K//2 - 1] = 1
    M[K//2 - 1][K//2 + 1] = -1
    M[K//2 - 1][K//2 - 1] = 1
    return M

"""
Funcion de convolucion recibe imagen y el los kernels kernel, k1, k2, k3 y k4
La imagen es recibida por un argumento se cambia a gris y se le anade el pading
Convoluciona la imagen con diferentes kernels y la grafica
"""

def convolucion(imagen, kernel, k1, k2, k3, k4):
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
        j1 = ndimage.convolve(I, k1, mode='constant', cval=0.0)
        j2 = ndimage.convolve(I, k2, mode='constant', cval=0.0)
        j3 = ndimage.convolve(I, k3, mode='constant', cval=0.0)
        j4 = ndimage.convolve(I, k4, mode='constant', cval=0.0)
        
        plt.figure(figsize=(30,30)) #Graficas
        
        plt.subplot(3,3,1)
        plt.imshow(Is)
        plt.xlabel('Input Image')

        plt.subplot(3,3,2)
        plt.imshow(j0)
        plt.xlabel('Gaussian Blur')

        plt.subplot(3,3,3)
        plt.imshow(j1)
        plt.xlabel('laplacian Of Gaussian')

        plt.subplot(3,3,7)
        plt.imshow(j2)
        plt.xlabel('Sobel Top')

        plt.subplot(3,3,8)
        plt.imshow(j3)
        plt.xlabel('Sobel Right')

        plt.subplot(3,3,9)
        plt.imshow(j4)
        plt.xlabel('Sobel Left')

        plt.tight_layout()
        plt.grid(False)
        plt.show()
        return
