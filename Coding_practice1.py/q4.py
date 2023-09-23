#Max Product
import numpy as np

def maxx(arr):
    maxi=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i]!=arr[j] and (arr[i]*arr[j])>maxi):
                maxi = arr[i]*arr[j]
    return maxi
l=np.array([1,8,2,3,4,5,6,7])
print(maxx(l))

