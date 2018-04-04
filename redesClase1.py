import numpy as np 
from numpy import sin, linspace, pi
from scipy.io.wavfile import read, write
from scipy import fft, arange, ifft

import matplotlib.pyplot as plt

rate, info=read("beacon.wav")
print(rate) #Frecuencia de muestreo
print(info)

dimension = info[0].size
print(dimension)

#data: datos del audio(arreglo de numpy)
if dimension == 1: 
	data = info
	perfect = 1
else: 
	data = info[:,dimension-1]
	perfect = 0

print("AAAAAAAAAAA")
print(data * 0.85)
print("ADSSADASDSA")


timp = len(data)/rate

t = linspace(0,timp,len(data))		#linspace(start,stop,number)
print(len(data))
print(timp)
plt.title('AUdio')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [dB]')
plt.plot(t, data)
plt.show()

large = len(data)
print(large)
print("asdsadas")
k = arange(large)
print(max(data))





#PARA CORRER:
#python3 prueba.p
