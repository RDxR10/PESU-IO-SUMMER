# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 03:24:02 2019

@author: Rishi
"""

def is_number(s):
    try:
        float(s)
        return True
    except (ValueError,TypeError):
        return False
    
s = input("Enter the string to be checked: ")
print(is_number(s))    