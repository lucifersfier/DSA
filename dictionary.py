'''A dictionary is a mutable collection of key value pairs where each unique key maps to the value'''
'''Dictionaries are implemented using hash tables which provide fast access to vvalues based on their keys '''

my_dict = dict()
print(my_dict)
my_dict2 = {}
print(my_dict2)
eng_sp = dict(one='uno',two='dos',three='tres')
print(eng_sp)

eng_sp2 = {'one':'uno','two':'dos','three':'tres'}
print(eng_sp2)   #Space and Time Complexity will be O(n)

eng_sp3_list = [('one','uno'),('two','dos'),('three','tres')]
eng_sp3 = dict(eng_sp3_list)
print(eng_sp3)

#Dictionary in a memory

'''A hash table is a way of doing key value lookups you store the values in an array
and then use a hash function to find the index of the array cell that corresponds to your key-value pair'''

#Insert/Update an element in an array

dictt = {'name':'nittyansh','age':22,'gender':'male'}
dictt['name']='shivansh'
print(dictt)

dictt['address']='Ghaziabad'
print(dictt)
'''Time and space complexity is O(1)'''

#Traversing through a dictionary 

def traverseDict(dictt):
    for key in dictt:   #------------------------>> O(n)
        print(key,dictt[key]) #------------------------>> O(1)
traverseDict(dictt)
'''Time and space complexity of the just above function is O(1) '''




