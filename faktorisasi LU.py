# -*- coding: utf-8 -*-
"""""
@author: Yobel hardongan panggabean 202010225052 TF3A1
"""

print ("Nama : Yobel hardongan panggabean")
print ("Kelas : TF3A1")
print ("Npm: 202010225052")


import scipy
from scipy.linalg import lu, lu_factor, lu_solve
import numpy as np

# definisikan matriks A
A = np.array([[3.,-0.1, -0.2], [0.1, 7., -0.3], [0.3, -0.2,10]])

# definisikan vektor b
b = np.array([7.85, -19.3, 71.4])

# solusi yang diberikan lu dan b
p, l , u = lu(A)
lu, piv = lu_factor(A)
x = lu_solve((lu, piv),b)
print ('matriks p :/n ',p)
print ('matriks l :/n ',l)
print ('matriks u :/n ',u)
print ('solutions:/n',x) 