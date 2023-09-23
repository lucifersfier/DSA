#Given 2D list calculate the sum of diagonal elements.

'''Example
myList2D= [[1,2,3],[4,5,6],[7,8,9]]  
diagonal_sum(myList2D) # 15'''
'''
def diagonal_sum(matrix):
    summ=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(i==j):
                summ+=matrix[i][j]
    return summ
myList2D= [[1,2,3],[4,5,6],[7,8,9]]  
print(diagonal_sum(myList2D))
l=[[3,2,1,5],[4,6,5,9],[8,9,7,10],[11,23,45,54]]
print(diagonal_sum(l))'''

#optimised solution is below now 
def diagonal_sum(matrix):
    summ=0
    for i in range(len(matrix)):
        summ+=matrix[i][i]
    return summ
myList2D= [[1,2,3],[4,5,6],[7,8,9]]  
print(diagonal_sum(myList2D))
l=[[3,2,1,5],[4,6,5,9],[8,9,7,10],[11,23,45,54]]
print(diagonal_sum(l))