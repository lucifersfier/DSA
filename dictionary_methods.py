mydict = {'fname': 'nittyansh','lname':'srivastava','age':'22','gender':'male','address':'Delhi'}

# (1) -->> The clear method doesn't take any parameter and it doesn't return any value, it return by default none

'''
mydict.clear()
print(mydict)
'''

# (2) -->> The copy method return sthe shallow copy of Dictionary 

dict = mydict.copy()
print(dict)

# (3) -->> The from keys method creates a new dictionary from given sequence of elements with value provided by user

newdict = {}.fromkeys([1,2,3],0) # a new dict with all the keys have same value
print(newdict)
ndict = {}.fromkeys([1,2,3]) # if we don't provide any value it will by default assigned as None
print(ndict)

# (4) -->> The gets method returns the value fir specified key if the key is in the dictionary

print(dict.get('age',23)) #if the value is not in dictionary it will give the present value in dictionary
print(dict.get('city','Raebareli')) # if the key doesn't exist in the dictionary it will return the specified value 

# (5) -->> The item method returns the view object that displays a list of dictionaries, key value tuple pairs.

print(dict.items())

# (6) -->> The keys method returns a view object that displays the list of all keys in the dictionary

print(dict.keys())

# (7) -->> The popitem method returns and removes an arbitrary element from the dictionary

print(dict.popitem())
print(dict)

# (8) -->> The setdefault method returns the value of key if key is in the dictionary if not it inserts key 
# with a value to the dictionary

print(dict.setdefault('address','ghaziabad'))
print(dict) 
print(dict.setdefault('age',23))


