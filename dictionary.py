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