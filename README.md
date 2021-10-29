# Evidencia-TC1001S.1 

Este repositorio esta hecho para la Semana Tec "Herramientas Computacionales: el arte de la programación" 
Con el fin de crear  un programa  en Python que procese imagenes, usando kernels, por medio de una convolución, y final mente un Padding.

# EQUIPO
Rodolfo de la O        A01366363   </br>
Jose Ortega Guido      A01770426 </br>
Fabian Gonzalez Vera   A01367585 </br>
Grettel Morales        A01769234 </br>

## Convolucion y Padding
La convolución es el como editamos una imagen, basicamente una imagen es una matriz, por otra matriz "kernel". </br>

El padding es para no perder informacion de la imagen, el paddinig es como un "marco" o una orilla que le ponemos a la imagen para que se vea de la mejor manera.


## Verbose

Verbose es muy importante ya que sirve para especificar que  información sera visualisada en patanlla. </br>

## Main 

El main funciona para juntar  las funciones de Laplace, Sobel y Gaussian Blur. Main principalmente lo que hace es importar todos los programas y ejecutar el correspondiente.


## Kernels 

### Laplace
Se implementaron dos funciones para crear un kernel de Laplace. Ambos kernel se usan para crear una imagen con bordes pronunciados. Debido a que es estado base, es muy sensible al ruido.

### Sobel
Sirve para detectar líneas y bordes en la imagen,funciona de forma similar a los kernels de detección de bordes, pero con una optimización de suavización, que permite que no se vean tan afectados por el ruido.

### Gauss Blur
Utilizando la función para crear un kernel Gaussiano, se obtiene un kernel que permite crear una imagen con ruido y detalle reducido

## LIB.py
El archivo `LIB.py`  funciona para generar todos los kernels mencionados, recibiendo x cantidad de parametros, los cuales son enviados desde el archivo main.py  </br>
Para el funcionamiento de la librería, se importa la librería de numpy, que se utiliza en la generación de matrices (kernels). </br>

## Instrucciones 
Para usar el programa se debe de abrir una consolas e ir al directorio donde se encuentran los archivos "main.py" y "LIB.py" ademas de que se debe de contar con la imagen a la cual se busca realizar las convoluciones en el mismo directorio. Una vez que se encuentre en el directorio dentro de la consola se debe de escribir el siguiente comando "python3 main.py image.jpg/png".

## Resultados 
Las images resultantes de la convolucion se puede observar a continuacion, fueron usadas las images "Sample.png" y "sudoku.png" que se encuentran en este mismo repositorio.
Las imagenes resultantes son las siguientes:
![Figure_1](https://user-images.githubusercontent.com/61805820/139489869-df7679de-3999-4348-b9da-be7030d9a479.png)


![Figure_2](https://user-images.githubusercontent.com/61805820/139489911-f7401e0b-cd2b-4ff2-98bf-134300dbda4f.png)



## Fuentes

http://blog.espol.edu.ec/telg1001/transformada-laplace-python/

https://en.wikipedia.org/wiki/Gaussian_blur

http://publib.boulder.ibm.com/tividd/td/TSMC/GC32-0788-04/es_ES/HTML/ans60000357.htm#:~:text=La%20opción%20verbose%20especifica%20que,se%20hace%20copia%20de%20seguridad.&text=Si%20especifica%20quiet%20en%20el%20archivo%20dsm.

https://programmerclick.com/article/6637654809/

https://benjaminva.github.io/semena-tec-tools-vision/

