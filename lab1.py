import numpy as np # Podríamos quitar este, ya que importa todo numpy y abajo importamos lo que nos sirve
from numpy import sin, linspace, pi

from scipy.io.wavfile import read, write
from scipy import fft, ifft, arange

import matplotlib.pyplot as plt

"""
 1. Importe la señal de audio utilizando la función read de scipy. 
 2. Grafique la función de audio en el tiempo
 3. Utilizando la transformada de fourier:
     a. Grafique la señal en el dominio de la frecuencia
     b. A la función en su frecuencia calcule la transformada de fourier inversa, compare con la señal original.
"""

# Función general para graficar, a lo que retorne podemos hacerle .show()
def makeGraphic(title, xlabel, xdata, ylabel, ydata):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(xdata, ydata)
    plt.savefig(title + ".png")
    return

def timeGraphic(data, rate):
    duration = len(data)/rate # Tiempo que dura todo el audio
    t = linspace(0, duration, len(data)) # Intervalos de tiempo de 0 a t, generando la misma cantidad de datos que hay en data o vector tiempo
    makeGraphic("Audio original", "Tiempo [s]", t, "Amplitud [dB]", data)
    return 

def freqGraphic(data, rate): # No sé si esté bien u.u
    fftData = fft(data)
    fftDataReal = abs(fftData)
    y = linspace(0, rate, len(fftDataReal))
    makeGraphic("Audio con TFF", "Frecuencia [Hz]", y, "Amplitud [dB]", fftDataReal)
    return fftData

def ifftGraphic(data, rate, fftData): # Aquí me deje llevar, no se porqie no funciona :(
    datas = len(data)
    duration = datas/float(rate)
    t = linspace(0, duration, datas)
    ifftData = ifft(fftData, datas)
    plt.plot(t, t)
    plt.title("IFFT")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud [dB]")
    plt.show()
    return
    

    
rate, info = read("beacon.wav")
print("El rate es:", rate) # Frecuencia de muestreo del archivo wav
print("La info es:", info) # Datos leídos del archivo wav

dimension = info[0].size
print("La dimension es:", dimension) # Cantidad de muestras y el número de canales de audio
print("Lo otro es:", info[0])

if(dimension == 1): # Esto se hace para dejar el audio en un arreglo de 1 dimensión
    data = info
else:
    data = info[:,dimension-1]

print("Graficando en dominio del tiempo")
timeGraphic(data, rate)
print("Graficando en dominio de la frecuencia")
fftData = freqGraphic(data, rate)
print("Graficando la inversa de la anterior")
ifftGraphic(data, rate, fftData)
print("Listo")


