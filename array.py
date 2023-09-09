import array

my_array = array.array('i')
print(my_array) #it will print the empty array with the type of integer 
my_array1 = array.array('i',[1,2,3,4,5,6,7,8])
print(my_array1)

'''
import numpy as np
np_array = np.array([1,2,3,4,5],dtype=int)
print(np_array)  '''


np_array1 = array.array('i',[1,2,3,4,5,6,7,89,100])
print(np_array1)
np_array1.insert(0,0)
print(np_array1)
np_array1.insert(3,9)
print(np_array1)
np_array1.insert(9,110)
print(np_array1)

#worst case for the inserting an element in an array is inserting the element in starting of the array 
#Time Complexitty = O(n) And Space Complexity = O(1)

from array import *
def traversing(arr):
    for i in range (len(arr)):
        print(int(arr[i]))

arr = array("d", [1, 2 ,3 ])
print(traversing(arr))  
#Time Complexity = O(n) and the Space Complexity = O(1)