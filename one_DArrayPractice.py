from array import *
import array
my_array = array.array('i',[1,2,3,4,5,6,7,8,9,0])
for i in my_array:
    print(i)

#*************************************#
print('Aceesing the value by index')
print(my_array[0])
print(my_array[6])
print(my_array[4])

#**************************************#

 
print("Apending the values in the given array ")
 
my_array.append(89)
print(my_array)

#Inserting the element in the array using insert() method

my_array.insert(0,21)
print(my_array)

#Extending the python array using extend method

my_array1 = array.array('i',[98,99,97,96,95,94,93,92])
my_array.extend(my_array1)
print(my_array)

#Adding items froms the list into an aray 
my_list=[ 1 ,  2 ]
my_array.fromlist(my_list)
print(my_array)

my_list1 = [1,3,4,7,9,10]
my_array1.fromlist(my_list1)
print(my_array1)

#Removing the element using remove() method

print("Removing the element using remove() method")

my_array.remove(21)
print(my_array)

#Remove last array element using pop() method
print("Remove last array element using pop() method")

my_array.pop()
print(my_array)

#Fetching anhy element through its index using index() method
print("Fetching anhy element through its index using index() method")
print(my_array.index(97))

#Reverse a python array using reverse() method
print("Reverse a python array using reverse() method")
my_array.reverse()
print(my_array)

#Get array buffer information through buffer_infomethod
print("Get array buffer information through buffer_info method")
print(my_array.buffer_info()) #first it will give starting point and second the number of elements

#Checking the number of occurrences of an element using count() method
print("Checking the number of occurrences of an element using count() method")
print(my_array.count(1))

#Converting array to list using tolist() method
'''print("Converting array to list using tolist() method")
print(my_array.tolist())'''

#Slice elements from an array
print("Slice elements from an array")
print(my_array[1:5])
print(my_array[:-1])
print(my_array[1:])
print(my_array[-1:])





