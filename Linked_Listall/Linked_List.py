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

###################### INSERTION IN SINGLY LINKED LIST IN MEMORY ############################

'''
1) - At the beginning of the linked list 
2) - After a node in the middle of linked list
3) - At the end of the linked list
'''

###################### INSERT AN ELEMENT AT THE END OF SINGLY LINKED LIST  ############################

'''
first create a new node
for that it have value and next pointer and in that case next pointer is null
'''
#next step
'''
update the last node's next pointer to point to the new node
'''
#last step 
'''
update the tail to pint to the new node
'''
#edge cases
'''
Ques - if there is not any element in the linked list and we try to call the append method to insert a new node at the end of the
       linked list, what will happen ?
Ans -  create a new node and then update head and tail to new node. 
'''        
#Linked List class for this empty singly linked list is going to be like this.

class Linked_List:
       
       def __init__(self):  #constructor
              self.head=None
              self.tail=None
              self.length=0
       def __str__(self):
              temp_node = self.head
              result = ''
              while temp_node is not None:
                     result += str(temp_node.value)
                     if temp_node.next is not None:
                        result += ' -> '
                     temp_node = temp_node.next
              return result
           
      # create the append method inside this linked list class
       def append(self,value): #this append method implies to the current instance of this object and then it will take value
          '''how can we identify the linked list is empty or not 
          if head pointer points to none in this case it means that it is empty, or if the length attribute that we have declared is zero
          then in this case list is empty'''
          new_node = Node(value)
          if self.head is None:
             self.head = new_node
             self.tail = new_node
          else:
             self.tail.next = new_node
             self.tail = new_node
                 
          self.length += 1 
          

    
newLinked_list = Linked_List()
newLinked_list.append(10)
newLinked_list.append(20)
        
          
###################### PRINT LINKED_LIST  __str__  ############################          

'''Now for printing Linked_list we are going to use __str__ method in python '''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

newLinked = Linked_List()
newLinked.append(10)
newLinked.append(20)
print(newLinked)




 
             
          
              

       
               
                     

   