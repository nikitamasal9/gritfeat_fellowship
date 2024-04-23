#Question 1:
#Reverse string using STACK
class Stack:
    def __init__(self):
        ''' 
        Initializing an empty stack
        '''
        self.items = []

    def push(self, item):
        '''
        Pushing an item onto the stack
          
        Args:
            item: the item that has to be pushed onto the stack 
        '''
        self.items.append(item)

    def pop(self):
        '''
        Popping and returning the item on the top of the stack
        
        Returns:
            The top item from the stack when stack is not empty and none when the stack is empty
        '''
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        '''
        Checking if the stack is empty
        
        Returns:
            True in case the stack is empty, else False
        '''
        return len(self.items) == 0

#defining the function for reversing the string using STACK
def reverse_string_using_stack(input_str):
    # Creating a stack object
    stack = Stack()
    
    # Pushing each character of the input string onto the stack
    for char in input_str:
        stack.push(char)
    
    # Initializing an empty string to store the reversed string
    reversed_str = ""
    
    # Popping each character from the stack and append it to the reversed_str
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    # Returning the reversed string
    return reversed_str

# Testing the function
input_str = "Hello"
result = reverse_string_using_stack(input_str)
print("Reversed String using Stack:", result)
