import argparse

import cv2

import LIB as lb
"""
Obtiene argumento de la imagen desde el shell "python3 main.py image.jpg/png"
"""
parser = argparse.ArgumentParser() 
parser.add_argument("echo", help="echo the image you use here")
args = parser.parse_args()
print(args.echo)

"""
Establece imagen como el argumento de args
Llama todas las funciones desde LIB y les da argumentos
"""

imagen = args.echo
k0 = lb.gauss_blur(k=7,sigma=1)
k1 = lb.laplacianOfGaussian(sigma=5,K=8)
k2 = lb.Sobel_Top(K=5)
k3 = lb.Sobel_right(K=5)
k4 = lb.Sobel_left(K=5)
con = lb.convolucion(imagen,k0,k1,k2,k3,k4)
