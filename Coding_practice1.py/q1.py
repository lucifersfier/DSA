#Solution to missing number 
import numpy as np
def find_missing(array,n):
    total = n*(n+1)/2
    return (total - sum(array))
arr = np.array([1,2,3,4,6])
print(find_missing(arr,6))

'''This function calculates the sum of the first n natural numbers using the arithmetic progression
formula and then subtracts the sum of the numbers in the array to find the missing number.
The time complexity of this function is O(n) because it iterates through the array once to calculate the
sum of its elements.'''
#