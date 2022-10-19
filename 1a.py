#Single Neuron

#inisialisasi numpy
import numpy as np

#inisialisasi variabel
#Input layer feature 10 
inputs = [4, 7, 3, 2, 8, 5, 6, 2, 6, 7]
#Neuron 1
weights = [0.3, 0.1, -0.4, 0.5, 0.6, 0.3, 0.2, 0.6, 0.3, -0.7]
#banyak bias tergantung dari berapa banyak neuron yang ada
bias = 6

#output dari rumus numpy
output = np.dot(weights, inputs) + bias

#print out
print(output)