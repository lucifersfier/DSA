def foo(array):
    sum = 0
    product = 1
    for i in array: # O(n)
        sum +=i
    for i in array: #O(n)
        product*=i
    print("sum = "+str(sum)+", Product = "+str(product))
    
    '''Time Complexity will be O(n+n)=O(n)'''