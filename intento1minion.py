#FAVOR DE OMITIR, SOLO ES UNA PRUEBA

import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage


Is = Image.open('minion3.png');
I = Is.convert('L');
I = numpy.asarray(I);
I = I / 255.0;


k0 = numpy.array([[0,-1,0],[-1,0,1],[0,1,0]])

'''
1 -1 1
-1 4 -1
 1 -1 1
'''

k1 = numpy.array([[0,0,0],[-1,0,1],[0,0,0]])

'''
 0 0 0
-1 0 1
 0 0 0
'''


k2 = numpy.array([[0,-1,0],[0,0,0],[0,1,0]])

'''
 0 -1 0
 0  0 0
 0  1 0
'''

J0 = ndimage.convolve(I, k0, mode='constant', cval=0.0)
J1 = ndimage.convolve(I, k1, mode='constant', cval=0.0)
J2 = ndimage.convolve(I, k2, mode='constant', cval=0.0)

plt.figure(figsize = (15,15))

plt.subplot(2,2,1)
plt.imshow(Is)
plt.xlabel('Input Image')

plt.subplot(2,2,2)
plt.imshow(J0)
plt.xlabel('VH direction')

plt.subplot(2,2,3)
plt.imshow(J1)
plt.xlabel('Horizontal direction')

plt.subplot(2,2,4)
plt.imshow(J2)
plt.xlabel('Vertical direction')


plt.grid(False)
plt.show()
