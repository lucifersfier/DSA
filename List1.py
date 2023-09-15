#A List is a data structure that holds an ordered collection of items
#When we traverse through empty list, it's not executed
#Lists are mutable data structures
#Now for inserting an element we use list methods : - insert(), append() and extend()

mylist = [1,2,3,4,5,6,7,8,9]
mylist.append(10)
print(mylist) 
mylist.insert(0,0)
print(mylist)
mylist1 = ['a','b','c','d','e','f','g']
mylist.extend(mylist1)
print(mylist)

#time and space complexity 
''' when we insert an element we have to move all the elements one step therefore time comlexitry will be O(n)
and time complexity for append operation is O(1) and for both the case space complexity is O(1)'''

'''time and space complexity for extend method is depend on number of elements on the list therefore we can say that 
time and space complexity will be O(n)'''   

#DELETING AN ELEMENT FROM THE LIST 
#We can delete elements from any position in our lists using pop keyword

mylist1.pop(1) #if you provide index it will delete the index element otherwise it will delete the last index element
print(mylist1)
mylist1.pop()
print(mylist1) #last element deleted
del mylist[2]
print(mylist)
print("deleting element using slicing in del method")
del mylist[:3]
print(mylist)

#remove method is useful when you know the elemeent itself
mylist.remove("a")
mylist.remove("c")
mylist.remove("d")
mylist.remove("f")
print(mylist)

'''if we don not use the paramenter in pop() method then time complexity will be O(1)
otherwise time complexitry will be O(n) & Space complexity for all the three method is O(1)'''

'''tIME COMPLEXITY FOR DEL() method is O(n)   '''
'''Remove method Time complexity is O(n)'''

