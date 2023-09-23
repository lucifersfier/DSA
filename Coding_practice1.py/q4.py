#Max Product
import numpy as np
'''
def maxx(arr):
    maxi=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i]!=arr[j] and (arr[i]*arr[j])>maxi):
                maxi = arr[i]*arr[j]
    return maxi
l=np.array([1,8,2,3,4,5,6,7])
print(maxx(l))
#here  time complexity is O(n*n)
'''
#optimise solution will be 

def max_product(arr):
    max1,max2=0,0
    for i in arr:
        if (i>max1):
            max1 = i
    for i in arr:
        if(i>max2 and i<max1):
            max2=i
    return max1*max2
l=np.array([1,12,2,3,10,5,89,7])
print(max_product(l))