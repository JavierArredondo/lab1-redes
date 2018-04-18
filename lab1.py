import numpy as np
from numpy import sin, linspace, pi

from scipy.io.wavfile import read, write
from scipy import fft, ifft, arange
from scipy.fftpack import fftfreq

import matplotlib.pyplot as plt
#import scipy.fftpack
#import scipy.fftpack.fftfreq

"""
Laboratorio 1 de Redes de Computadores por Shalini Ramchandani & Javier Arredondo
 1. Importe la señal de audio utilizando la función read de scipy. 
 2. Grafique la función de audio en el tiempo
 3. Utilizando la transformada de fourier:
     a. Grafique la señal en el dominio de la frecuencia
     b. A la función en su frecuencia calcule la transformada de fourier inversa, compare con la señal original.
"""
###################################################
############# Definición de funciones #############
###################################################
"""
Función que gráfica los datos en xdata e ydata, asignándole el valor a cada eje,
por otro lado se le asigna un título a dicho gráfico.
Entrada:
    title  -> Título del gráfico
    xlabel -> Etiqueta del eje y
    xdata  -> Datos del eje x
    ylabel -> Etiqueta del eje y
    ydata  -> Datos del eje y
Salida:
    None
"""
def makeGraphic(title, xlabel, xdata, ylabel, ydata):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(xdata, ydata)
    plt.savefig(title + ".png")
    return

"""
Función que gráfica el audio en dominio del tiempo. Para esto se adquiere la duración del audio (1)
y el tiempo en segundos para cada dato en el rate (2). Posteriormente se gráfica el contenido del audio.
Entrada:
    data -> Son los datos obtenidos al leer el audio
    rate -> Frecuencia de muestreo del archivo wav
Salida:
    None
"""
def timeGraphic(data, rate):
    duration = len(data)/rate            # (1)
    t = linspace(0, duration, len(data)) # (2)
    makeGraphic("Audio original", "Tiempo [s]", t, "Amplitud [dB]", data)
    plt.show()
    return 

"""
Función que gráfica el audio en dominio de su frecuencia. Para esto es necesario calcular la transformada de fourier
de la librería de scipy y secuencia de valores de los datos obtenidos.
Entrada:
    data -> Son los datos obtenidos al leer el audio
    rate -> Frecuencia de muestreo del archivo wav
Salida:
    None
"""
def freqGraphic(data, rate):
    sample = len(data)
    fftData = fft(data) / sample
    fftFreqs = np.fft.fftfreq(sample, 1/rate) # Return the Discrete Fourier Transform sample frequencies.
    makeGraphic("Audio con FFT", "Frecuencia [Hz]", fftFreqs, "Amplitud [dB]", abs(fftData))
    plt.show()
    return fftData

"""
Función que gráfica la transformada inversa del audio, por lo tanto queda en el dominio del tiempo. Para esto se utiliza la librería
de scipy.
Entrada:
    data    -> Datos obtenidos del audio
    rate    -> Frecuencia de muestreo de los datos obtenidos.
    fftData -> Datos de la transformada de fourier del audio.
"""
def ifftGraphic(data, rate, fftData):
    sample = len(data)
    duration = sample/rate
    t = linspace(0, duration, sample)
    ifftData = ifft(fftData)*len(fftData)
    makeGraphic("Audio con IFFT",  "Tiempo [s]", t, "Amplitud[dB]", ifftData)
    plt.show()
    return ifftData
    

def truncatedGraphic(fftData,rate):
    maximum = max(fftData)
    print("maximo: ",maximum)

    newData = np.zeros(len(fftData))

    index = 0
    done = 0
    for data in fftData:
        if fftData[index] == maximum:
            if done == 0:
                done = 1
            else:
                maxFreq = index
                break
        else:
            index = index + 1    
        
    maxInterval = round(index + index*0.15)
    minInterval = round(index - index*0.15)

    newData[minInterval:maxInterval] = fftData[minInterval:maxInterval]

    fftFreqs = np.fft.fftfreq(len(fftData), 1/rate) # Return the Discrete Fourier Transform sample frequencies.    

    makeGraphic("Audio con FFT truncado al 15%",  "Frecuencia [Hz]", fftFreqs, "Amplitud[dB]",abs(newData))
    plt.show()   
    return newData
        
    

rate, info = read("beacon.wav")
#print("El rate es:", rate) # Frecuencia de muestreo del archivo wav
#print("La info es:", info) # Datos leídos del archivo wav

dimension = info[0].size
#print("La dimension es:", dimension) # Cantidad de muestras y el número de canales de audio
#print("Lo otro es:", info[0])

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
print("Graficando en dominio de frecuencia truncado")
truncatedData = truncatedGraphic(fftData,rate)
print("Graficando la inversa del truncado")
ifftGraphic(data, rate, truncatedData)
print("Listo")


