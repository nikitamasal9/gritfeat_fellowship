# Creating a class named Node which is a basic building block for a linked list 
class Node:
    def __init__(self, data):
        '''
        Initializing a node object with the given data.
        
        Args:
            data: The data to be stored in the node.
        '''
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        '''
        Initializing an empty linked list
        '''
        self.head = None

    def append(self, data):
        '''
        Appending a new node with the given data to the end of the linked list.
        
        Args:
            data: The data to be stored in the new node.
        '''
        new_node = Node(data)
        if self.head is None:
            # if the linked list is empty, head is the new node
            self.head = new_node
            # exiting the method immediately after setting head to new node
            return
        # traversing to the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        # appending new node to the end of the linked list
        last_node.next = new_node

    def reverse(self):
        '''
        Reversing the order(reference) of nodes in the linked list
        '''
        prev = None
        current = self.head
        while current:
            # storing next reference of current node in next node
            next_node = current.next
            # storing previous reference to next reference of current node
            current.next = prev
            # moving previous and current references one step further
            prev = current
            current = next_node
        # setting the head to prev(after loop, it is the last node), which becomes the new head after reversal
        self.head = prev

    def display(self):
        '''
        Displaying the elements of the linked list
        '''
        current = self.head
        while current:
            # printing the data of the current node
            print(current.data, end="")
            # moving to the next node
            current = current.next
        print()

def reverse_string_using_linked_list(input_str):
    '''
    Reversing a string using a LINKED LIST
    
    Args:
        input_str: the input string to be reversed
        
    Returns:
        the reversed string'''
    
    # creating a linked list object 
    linked_list = LinkedList()
    # appending each character of the input string to the linked list
    for char in input_str:
        linked_list.append(char)
    # reversing the linked list
    linked_list.reverse()
    # initializing output string reversed_str
    reversed_str = ""
    current = linked_list.head
    while current:
        # getting the reversed string by traversing the reversed linked list
        reversed_str += current.data
        current = current.next
    return reversed_str

# Test the function
input_str = "Hello"
result = reverse_string_using_linked_list(input_str)
print("Reversed String using Linked List:", result)