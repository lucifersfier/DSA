'''what is the run time of the below code'''
def printunorderedpair(arrayA,arrayB):
    for i in range(len(arrayA)):     #---------------> O(ab)
        for j in range(len(arrayB)): #------------------> O(b)
            if(arrayA[i]<arrayB[j]): #---------------------> O(1)
                print(str(arrayA[i])+","+str(arrayB[j]))
                
x=[1,2,3,4,5,6,78,9]
y=[3,4,5,67,2,3,4,5]
print(printunorderedpair(x,y))

'''Time Complexity will be O(ab) if the length of arrayA is 'a' and the length of arrarB is 'b' '''
#