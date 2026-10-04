#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:52:26 2026

@author: ignacioferris
"""
import numpy as np

# =========================
# CARGAMOS LAS MATRICES
# =========================

I_real = np.load("matriz_gris_1.npy")
I_IA = np.load("matriz_gris_IA_1.npy")

print("Imagen real:", I_real.shape)
print("Imagen IA:", I_IA.shape)


# =========================
# TRANSFORMADA DE FOURIER 2D
# =========================

F_real = np.fft.fft2(I_real)
F_IA = np.fft.fft2(I_IA)


# =========================
# CENTRAMOS LAS FRECUENCIAS
# =========================

F_real_centrada = np.fft.fftshift(F_real)
F_IA_centrada = np.fft.fftshift(F_IA)




#Por ahora solo tomamos las frecuencias absolutas
magnitud_real = np.abs(F_real_centrada)
magnitud_IA = np.abs(F_IA_centrada)



#Visualizamos fouriuer


import matplotlib.pyplot as plt

# Módulo
magnitud_real = np.abs(F_real_centrada)
magnitud_IA = np.abs(F_IA_centrada)

# Logaritmo para poder visualizar
espectro_real = np.log1p(magnitud_real)
espectro_IA = np.log1p(magnitud_IA)




# =========================
# MOSTRAR IMAGEN REAL
# =========================

plt.figure()
plt.imshow(espectro_real, cmap="gray")
plt.title("Espectro de Fourier - Real")
plt.colorbar()
plt.show()


# =========================
# MOSTRAR IMAGEN IA
# =========================

plt.figure()
plt.imshow(espectro_IA, cmap="gray")
plt.title("Espectro de Fourier - IA")
plt.colorbar()
plt.show()