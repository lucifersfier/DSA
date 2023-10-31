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

################## INSERT METHOD IN SINGLY LINKED LIST ####################

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
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
        
    def Insert(self,index,value):
        newnode = Node(value)
        if index<0 or index>self.length:
            return False
        elif self.length == 0:
            self.head=newnode
            self.tail = newnode
        elif index == 0:
            newnode.next = self.head
            self.head = newnode
        else:
            tempnode = self.head
            for _ in range(index-1):
                tempnode = tempnode.next
            newnode.next = tempnode.next
            tempnode.next = newnode
        self.length += 1
        return True
        
new = LinkedList()
new.Insert(0,30)
new.append(10)
new.append(20)            
new.append(30)
print(new)
new.Insert(0,9)
print(new)
    
'''Time & Space Complexity of the Insert function is O(n) and O(1) respectively.'''
    