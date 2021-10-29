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

def laplacianOfGaussian(sigma, K):
    M = numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            M[x][y] = -(1/(numpy.pi*sigma**4)) * (1-((x**2+y**2)/(2*sigma**2))) \
                        * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return M

def met_sobel(image, size, verbose=False): #Kernel Sobel
    vertical = np.array([[1],[2],[1]])
    horizontal = np.array([[1,0,-1]])
    filter3 = vertical*horizontal
    if size == 3:
        filter = filter3
    else:
        filter = filter3
        while size > 3:
            horizontal2 = np.array([[1,2,1]])
            filter = signal.convolve2d(vertical*horizontal2, filter)
            print("Kernel  Metodo Sobel : ")
            print(filter)
            size = size - 2
    
    #Convolucion 
    disp1 = convolution(image, filter, verbose)

    if verbose:
        plt.imshow(disp1, cmap='gray')
        plt.title("Horizontal Edge")
        plt.show()

    disp2 = convolution(image, np.flip(filter.T, axis=0), verbose)

    if verbose:
        plt.imshow(disp2, cmap='gray')
        plt.title("Vertical Edge")
        plt.show()
  
    gradient_magnitude = np.sqrt(np.square(disp1) + np.square(disp2))

    gradient_magnitude *= 255.0 / gradient_magnitude.max()
    
    if verbose:
        plt.imshow(gradient_magnitude, cmap='gray')
        plt.title("Gradient Magnitude")
        plt.show()

    return gradient_magnitude

def convolucion(imagen, kernel, k1, k2): #Convolucion de imagen
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
	j1 = ndimage.convolve(I, k2, mode='constant', cval=0.0)
        
        plt.figure(figsize=(15,15)) #Graficas
        plt.subplot(3,3,1)
        plt.imshow(Is)
        plt.xlabel('Input Image')

        plt.subplot(3,3,2)
        plt.imshow(j0)
        plt.xlabel('Gaussian Blur')
	
	plt.subplot(3,3,3)
        plt.imshow(j1)
        plt.xlabel('laplacian Of Gaussian')
	
	plt.subplot(3,3,4)
        plt.imshow(j2)
        plt.xlabel('Sobel')
        
        plt.grid(False)
        plt.show()
        return

