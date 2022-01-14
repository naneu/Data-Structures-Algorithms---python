
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end="->")
            temp = temp.next
    #adding a node at the end of the list
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True
    #adding a node infront of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True
    # remove an item from the tail end O(n)
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            while temp.next:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
        self.length -= 1
        return temp

    #Removing an item from the beginning of a Linked List O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None

        self.length -= 1
        return temp
    #get the node at a give index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
    #set the value of a node 
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value

            return True
        return False

    #insert a node at a given index
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)

        new_node.next = temp.next
        temp.next = new_node

        self.length += 1
        
        return True

    #remove a node from a list
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

    #reverse the list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        return True


my_sll = SinglyLinkedList(1)
my_sll.append(2)
my_sll.prepend(0)
my_sll.set_value(0, 3)
my_sll.insert(3,4)
my_sll.reverse()

my_sll.print_list()
