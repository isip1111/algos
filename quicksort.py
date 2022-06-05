# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 23:27:57 2022

@author: jerem
"""

def partition1(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1], arr[high] = arr[high],arr[i+1]
    return i + 1
    
def quick_sort(arr, low, high):
    if low < high:
       pivot = partition1(arr, low, high)
       quick_sort(arr, low, pivot-1)
       quick_sort(arr, pivot+1,high)

number = [5, 4, 3, 2, 1]
quick_sort(number,0,len(number)-1)
print(number)
