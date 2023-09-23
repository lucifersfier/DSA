#write a program to find all pairs of integers whose sum is equal to a given number(distinct pair)
import numpy as np
def summ(arr,value):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]==arr[j]):
                continue 
            elif(arr[i]+arr[j]==value):
                print(i,j)
l=np.array([1,2,3,4,5,6,7,8])
print(summ(l,6))
            
            
    
    