# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 03:01:59 2019

@author: Rishi
"""
N= int(input("Enter Any Integer: "))
S= 0

while(N>0):
    R = N % 10
    S = S + R
    N = N//10

print("Sum of the digits of the given integer = ",S)