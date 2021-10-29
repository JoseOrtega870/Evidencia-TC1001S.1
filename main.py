import argparse
import cv2
import LIB as lb


parser = argparse.ArgumentParser() #Obtiene argumento de la imagen del shell "python3 main.py image.jpg/png"
parser.add_argument("echo", help="echo the image you use here")
args = parser.parse_args()
print(args.echo)

#Generate the kernel for each image convolution
kernelTS = lb.topSobel(3) #Size of kernel
kernelRS = lb.rightSobel(3) #Size of kernel
kernelLS = lb.leftSobel(3) #Size of kernel


imagen = args.echo
#image=int(imagen)
k0 = lb.gauss_blur(k=7,sigma=1)
k1 = lb.laplacianOfGaussian(sigma=5,K=8)
k2 = lb.topSobel(K=5)
k3 = lb.rightSobel(K=5)
k4 = lb.leftSobel(K=5)
con = lb.convolucion(imagen,k0,k1,k2,k3,k4)
