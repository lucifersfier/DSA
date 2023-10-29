#)-Linked list is a form of sequential collection and it doesn't have to be in order
'''A Linked list is made up of independent nodes that may contain any type of data and
   each node has a reference to the next node in the link'''

#Differences between python list and Linked list --->>>>>>>>>>

#1) - pyhton list have indexes but linked list we don't have indexes
#2) - Elements are contiguous with each other but in linked they aren't contiguous so elements are located next to each 
#     other in liked list.

'''TYPES OF LINKED LIST--------->>>>>>>>'''

'''
a - Singly Linked List
b - Circular Singly Linked List
c - Doubly Linked List
d - Circular doubly linked list
''' 

###################### NODE CLASS CONSTRUCTOR ############################
'''   
       10 -->> 20 -->> 30 -->> 40 -->> None 
      (head)                  (tail)
      
      (1) - Node is not only the value, but also the pointer to the next node
            You can think it as a Dictinary well It's not exactly as a dictionary, but to make things easier 
            and understandable, we can think of this as a dictionary so that value is going to be the key and 
            the next key is going to be the pointer.
            
            {
               "value":10
               "next":None
            } 
            
'''

class Node:
   #now we need to construct the constructor so in the constructor we will have the attributes of the node.
   def __init__(self,value):
          #initialize the attributes
          self.value = value
          self.next = None

new_node = Node(10)
print(new_node)   # Showing the location in the memory as output
'''it is not printing the value because we have not defined any method for printing out this node here'''
#That's how we are creating the node class for the linked list
#***********************************************************************************
'''Time and Space Complexity for the class Node --->>>>>  is O(1)      '''
#***********************************************************************************


###################### LINKED LIST CONSTRUCTOR -->> CREATION OF SINGLY LINKED LIST ############################

# class LinkedList:
#        def __init__(self,value):
#               new_node = Node(value)
#               self.head = new_node
#               self.tail = new_node
              
#class LinkedList:
#      def __init__(self):
#         self.head = None
#        self.tail = None #Empty linked list 
         
class Node:
   def __init__(self,value):
      self.value = value
      self.next = None
      
class LinkedList:
   def __init__(self,value):
          new_node = Node(value)
          self.head = new_node
          self.tail = new_node
          self.length = 1
          
new_linked_list = LinkedList(10)
print(new_linked_list.head.value)
print(new_linked_list.length)

'''Time & Space complexity for creating the linked list is O(1)'''




          
      
       
               
                     

   