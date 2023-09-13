import numpy as np
tda = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(tda)
#time complexity of this operation is O(m*n)
ntda = np.insert(tda,0,[[4,3,2,1]],axis=1) #here if you want add column then axis =1 otherwise for row axis = 0 
print(ntda) #2nd position in np.insert(tda,0,[[4,3,2,1]],axis=1) tells about the position where you want to insert the column or row 


#******************************#

#by using append function we can app new row or column in the given array

t_da = np.array([[9,8,7,6],[5,4,3,2]])
nt_da = np.append(t_da,[[2,1,0,0]],axis= 0)
print(nt_da)

#Accessing an element of two dimensional array
def AcessElements(array,rowindex,colindex):
    if rowindex>=len(array) and colindex>=len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowindex][colindex])
print("Acessing the element")
AcessElements(tda,1,2)  # time complexity is O(1)

#************************#
print("traversing through two dimensional array")
def Travrsing(array):
    for i in range(len(array)):
        for j in range ( len(array[0])):
            print(array[i][j])
Travrsing(tda)  # Time complexity will be O(mn) & space complexity will be O(1) 

#*************************************#
print("Searching for an element in two dimensional array")
def Serarching(array,element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if(array[i][j]==element):
                print("found"+"",i,j)

                
Serarching(tda,13)

#****************************************#




    
    
    

