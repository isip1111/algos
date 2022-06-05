# -*- coding: utf-8 -*-
"""
Created on Fri May 27 21:22:53 2022

@author: jerem
"""

def bub_sort(arr):
    for i in arr:
        print(arr)
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                

if __name__ == '__main__':
    numbers = [3,4,5,1,2]
    print(numbers)
    bub_sort(numbers)
    print(numbers)
    

