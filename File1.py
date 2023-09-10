def fact(n):
    if n<=0:
        return 1                   
    return n*fact(n-1)
print(fact(6))
''' Methods like this which are calling themselves recursively count in the space so it is going to be
added in the memory to be remembered to come back to the last call'''             

    
        