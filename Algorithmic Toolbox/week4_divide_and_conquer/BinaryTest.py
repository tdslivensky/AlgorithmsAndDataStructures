# Uses python3
import sys
import math

def binary_search(a, low, high, x):
    if high < low:
        return -1

    mid = low + math.floor((high-low) / 2)

    if(a[mid] == x):
        return mid
    elif (x > a[mid]):
        return binary_search(a, mid + 1, high, x)
    elif(x < a[mid]):
        return binary_search(a, low, mid - 1, x)

if __name__ == '__main__':
    arr = [1,5,8,12,13,23]
    search = [8,1,23,1,11,24]
    low = 0 
    high = len(arr) - 1
    for x in search:
        # replace with the call to binary_search when implemented
        print(binary_search(arr, low, high, x), end = ' ')