'''What is the run time of the below code'''

def printpairs(array):
    for i in array:     #-------------------------->>> O(n)
        for j in array: #------------------------------>>> O(n)
            print(str(i)+","+str(j))
            
'''there is a nested loop which means operation will be performed for each n, n times 
Time Complexity Will be O(n**2)'''