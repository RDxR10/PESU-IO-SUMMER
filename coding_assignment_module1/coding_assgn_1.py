# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

vals = input().split(",")
n_vals=[]
for _ in vals:
    n_vals.append(int(_))
        
print(n_vals)
print(tuple(n_vals))