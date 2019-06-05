# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:01:13 2019

@author: Rishi
"""

#
#import bisect
#l = input("Enter a list of numbers").split(" ")
#l_vals=[]
#for _ in l:
#    l_vals.append(int(_))
#x = int(input("Enter the no. you want to search"))
#sorted(l_vals)
#print(bisect.bisect_left(l_vals,x))



def binarySearch(list, x): 
    l = 0
    r = len(list)-1
    while l<= r: 
  
        mid = int((l+r)/2) 
          
    
        if list[mid] == x:
            
            return mid 
  
        
        elif list[mid] < x: 
            l = mid + 1
  
        
        else: 
            r = mid - 1
      
    
    return -1


l = input("Enter a list of numbers").split(" ")

l_vals=[]
for _ in l:
    l_vals.append(int(_))
#sorted(l_vals)    
x = int(input("Enter the element you want to search"))

result = binarySearch(l_vals,x) 
if(l_vals == sorted(l_vals)):
    if result != -1: 
        print("Element is present at index",result) 
    else: 
        print("Element is not present in list")
else:
    print("Elements aren't sorted in list. Do you want them to be sorted?(Y/N)")
    decision=None
    while True:
        decision = input()
        if str(decision)=='Y':
            print("Here's your sorted list", sorted(l_vals))
            result = binarySearch(sorted(l_vals),x)
            if result != -1:
                print("Element is present at index",result)
            else:
                print("Element is not present in list")
        elif str(decision)=='N':
            print("Okay")
        else:
            print("Y/N?")
        
    
        