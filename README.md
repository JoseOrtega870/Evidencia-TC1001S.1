# Evidencia-TC1001S.1 

Este repositorio esta hecho para la Semana Tec "Herramientas Computacionales: el arte de la programación" 
Con el fin de crear  un programa  en Python que procese imagenes, usando kernels, por medio de una convolución, y final mente un Padding.

# EQUIPO
Rodolfo de la O A01366363   </br>
Jose Ortega Guido A01770426 </br>
Fabian Vera       A01367585 </br>
Grettel Morales   A01769234 </br>


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
