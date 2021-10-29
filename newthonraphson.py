# -*- coding: utf-8 -*-
"""
@author: Yobel hardongan panggabean 202010225052 TF3A1
"""

print ("")
print ("")
print ("Nama : Yobel hardongan panggabean")
print ("Kelas :  TIF3A1")
print ("NPM : 202010225052")
print ("")
print ("")

import numpy as np
import matplotlib.pyplot as plt
from math import e #Untuk memanggil bilangan eksponen natural (e)
# Mendefinisikan  fungsi
def f(x):
    return e**x-5*x**2
#Mendefinisikan Turunan Fungsi
def DF(x):
    return e**x-10*x
#Metode Newton-Raphson
def newtonRaphson(x0,eps):
    step = 0
    print('\n\n*** --Metode Newson Raphson-- ***')
    xn = x0
    for n in range(0,100): #Maksimal iterasi adalah 100
        fxn=f(xn)
        if abs(fxn) < eps:
            print('\n Akar Persamaan tersebut : %0.8f' % xn)
            return xn
        Dfxn=DF(xn)
        if Dfxn == 0:
            print('Solusi tidak ditemukan')
            return None
        xn=xn-(fxn/Dfxn)
        step = step + 1
        print('Iterasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, xn, f(xn)))
    print('Iterasi maksimum, solusi tidak di temukan')
#Sesi Input Nilai awal yang di konversi kepecahan
x0 = float(input('x0: '))
eps = float(input('epsilon : '))
newtonRaphson(x0,eps)
