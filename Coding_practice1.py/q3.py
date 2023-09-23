#checking a number is exist in the array or not 
import numpy as np
def Search(array,value):
    if(value in array):
        return True
    else:
        return False        
arr=np.array([1,2,3,4,5,65,433,5,656,32])
print(Search(arr,656))

        