'''#Tuple operations and methods ------>>>>>>>>'''

mytup=(1,2,3,7,5)
yourtup=('a','b','c','d','e')
tup=tuple('123456')
'''print(mytup)
print(yourtup)
print(tup)
'''
#(1) -->> Concatenation

print(mytup + tup)
print(yourtup + mytup)
print(mytup + yourtup + tup)

#(2) -->> Star operator

print(mytup * 3)

#(3) -->> Only two methods available for tuple -->> (a) Count and (b) index method

print(mytup.count(3))
print(mytup.index(7))

''' Built in functions for Tuple'''

# (1) ---->>>> len()

print(len(mytup))

# (2) ---->>> max()

print(max(mytup))

# (3) ---->>>> list into tuple

l=[1,2,3,4,5,6,7,8,9,0,10]
print(tuple(l))

