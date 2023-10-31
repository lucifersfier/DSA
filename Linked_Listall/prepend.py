'''class Node:
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
'''
###################### INSERT AN ELEMENT AT THE BEGINNING OF THE LINKED lIST - PREPEND METHOD ###################
'''function to create nodes'''
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
'''function to create Linked List'''
class LinkedList:
    '''initializing empty linked list'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    '''function to represent the Linked List '''
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    '''function to append the elements in the linked list'''
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    '''funtion to prepend the elements in the linked list'''    
    def prepend(self,value):   #------------->>> O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
            
new = LinkedList()
new.append(10)
new.append(20)            
new.append(30)
print(new)
new.prepend(4)
print(new)
        
'''Time and Space Complexity of the prepend function of the linked list is O(1)'''       