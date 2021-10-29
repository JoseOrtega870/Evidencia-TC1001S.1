def met_sobel(image, size, verbose=False):
    #Definimos parametros del kernel
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
