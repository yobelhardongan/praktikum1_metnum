#Yobel hardongan
#202010225052
# Interpolasi Lagrange

import numpy as np

# Membaca Jumlah Titik Data

n = int(input('Masukkan Jumlah titik data : '))

#Membuat array ukuran n x n dan inisiasi
x = np.zeros((n))
y = np.zeros((n))

#Membaca Titik Data
print('Masukkan data x dan y : ')
for i in range (n):
    x[i] = float(input( 'x[' + str(i)+']= '))
    y[i] = float(input( 'y[' + str(i)+']= '))

# Membaca Interpolasi Titik
xp = float(input('Masukkan x yang Diinginkan : '))

#Inisiasi Interpolasi
yp = 0

#Implementasi Interpolasi Lagrange
for i in range(n):

    p = 1

    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])

    yp = yp + p * y[i]

# Displaying Output
print('Nilai Interpolasi untuk %.3f adalah %.3f.' %(xp, yp))
print('Yobel hardongan 202010225052')