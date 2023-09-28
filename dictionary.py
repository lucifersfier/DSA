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
'''Time and space complexity of the just above function is O(n) and O(1) '''

#Search for an element in a Dictionary 

def SearchDictt(dict,value):
    for key in dict:
        if(dict[key]==value):
            return key, value
    return "The Value doesn't exist"
print(SearchDictt(dictt,22))
print(SearchDictt(dictt,23))

'''Time and space complexity for just above the function is O(n) and O(1)'''

#Remove/Delete an element from the dictionary

del dictt['address']
print(dictt)
'''time complexity for deleting an element from the dictionary is O(1) because it uses hash table'''
'''Space complexity is also O(1)'''
'''another method to remove a key-value pair from a dictioanry is pop method
this method is also returns the value associated with the key
and if the key is not found, it returns a default value that is provided otherwise it's going to raise 
key error'''


remv = dictt.pop('gender')
print(remv)
print(dictt)

'''if we write like this 'remv = dictt.pop('gen',None)' and we didnt found any key or value 
in the dictionary then it will not give an error so always make sure to provide parameters so that program can run smoothly'''
#remv = dictt.popitem() then it will delete the last key value pair from the dictionary
#Clear method removes all key value pairs from the dictionary dictt.clear() and then print(dictt) 
# it will show empty dictionary Time and space complexity is O(n) and O(1) 
'''Time and Space Complexity is O(1)'''

