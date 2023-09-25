'''what willl be the runtime orf this code'''
def func(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1    # ------------------------>>>>> O(n/2) = O(n)
        tremp = array[i]          # ------------------------>>>>> O(1)
        array[i] = array[other]   # ------------------------>>>>> O(1)
        array[other] = tremp      # ------------------------>>>>> O(1)
    print(array)                  # ------------------------>>>>> O(1)
l=[1,2,3,4,5,6,78,9]              
print(func(l))
'''Time Complexity will be O(n)'''