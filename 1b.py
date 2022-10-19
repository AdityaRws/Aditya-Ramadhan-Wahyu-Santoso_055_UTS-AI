#Multi Neuron

#inisialisasi numpy
import numpy as np

#inisialisasi variabel
#Input layer feature 10 
inputs = [2.0, 0.4, 2.0, 0.43, -4.0, 0.22, 4.0, 7.0, 4.0, 11.0]

#Neuron 5
weights = [[3.0, 9.0, 3.0, 0.4, 0.7 0.4, 0.2, 0.4, 0.9, -0.1],
[0.12, 0.24, 0.54, 0.2, 0.8, 0.25, -2.0, 0.33, 0.89, 0.46],
[0.32, 0.5, 0.3, 0.23, 0.24, -0.29, -0.46, 0.78, 0.99, -0.1],
[2.0, 0.21, 0.3, 7.0, 6.0, 2, 6, 0.55, 0.33, 0.22],
[1.0, 0.2, -2.0, 2.0, -0.2, -0.47, 1.0, -0.7, 0.4, -0.36]]

#banyak bias tergantung dari berapa banyak neuron yang ada
biases = [7.0, 6.0, 3.0, 4.0, 2.0]

#output dari rumus numpy
output = np.dot(weights, inputs) + biases

#print out
print(output)