#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:05:43 2026

@author: ignacioferris
"""

from PIL import Image
import numpy as np

imagen = Image.open("imagenIA_1.png")

imagen_gris = imagen.convert("L")
I = np.array(imagen_gris)

print("Antes:", I.shape)

I = np.rot90(I, k=1)  # o k=3 según la orientación

print("Después:", I.shape)

np.save("matriz_gris_IA_1.npy", I)
