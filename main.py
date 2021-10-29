import argparse
import cv2
import LIB as lb


parser = argparse.ArgumentParser() #Obtiene argumento de la imagen del shell "python3 main.py image.jpg/png"
parser.add_argument("echo", help="echo the image you use here")
args = parser.parse_args()
print(args.echo)

imagen = args.echo
k0 = lb.gauss_blur(k=7,sigma=1)
con = lb.convolucion(imagen,k0,k1)
k1 = lb.laplacianOfGaussian(sigma=5,K=8)
k2 = lb.met_sobel(image,3,verbose=FALSE)
