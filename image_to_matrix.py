#!/usr/bin/env python3
# -*- coding: utf-8 -*-


##Construcion de matrices de escalade grises a partir de imagenes


"""
Created on Mon Aug 10 19:02:41 2026

@author: ignacioferris
"""



#Trasformamos la imagen en una matriz RGB




from PIL import Image
import numpy as np

# Abrimos la imagen
imagen = Image.open("imagen_1.png")
#imagen = Image.open("imagenIA_1.png")
I_RGB = np.array(imagen)
#print(I_RGB) #Imagen en RGB




# Convertimos a escala de grises
imagen_gris = imagen.convert("L")

# Convertimos la imagen en una matriz
I = np.array(imagen_gris)

#print(I)
print(I.shape)
#print(I_RGB)



#Matriz completa
#np.set_printoptions(threshold=np.inf)

#print(I)

np.save("matriz_gris_1.npy", I)
#np.save("matriz_gris_IA_1.py", I)
