class Node:
    def __init__(self, data):
        '''
        Initializing a Node object with the given data.

        Args:
            data: The data to be stored in the node.
        '''
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        '''
        Initializing an empty Stack.
        '''
        self.top = None

    def isempty(self):
        '''
        Checking if the stack is empty.
        '''
        if self.top == None:
            print("Stack is empty")
        else:
            print("Stack is not empty")
        
    def push(self):
        '''
        Pushing an element onto the top of the stack.
        '''
        x = int(input("Enter element to push into the stack:"))
        new = Node(x)
        if self.top == None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        '''
        Popping an elemet from the top of the stack.
        '''
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print("The popped element is: ", self.top.data)
            self.top = None
        else:
            temp = self.top
            print("The popped element is: ", self.top.data)
            self.top = temp.next
            temp = None

    def display(self):
        '''
        Displaying all the elements in the stack.
        '''
        if self.top is None:
            print("Stack is empty")
        else:
            print("Elements in the stack are: ")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    def peek(self):
        '''
        Displaying the element at the top of the stack without removing it.
        '''
        if self.top is None:
            print("Stack is empty")
        else:
            print("Element on the top of the stack: ", self.top.data)



#Testing:
s = Stack()
while(1):
    print("Enter the options from below")
    print("1-Push operation \n 2-Pop operation \n 3-IsEmpty operation \n 4-Display \n 5-Peek operation \n 6-Exit")
    option = int(input())
    if option == 1:
        print("Push operation")
        s.push()
    elif option == 2:
        print("Pop operation")
        s.pop()
    elif option == 3:
        print("IsEmpty operation")
        s.isempty()
    elif option == 4:
        print("Display")
        s.display()
    elif option == 5:
        print("Peek operation")
        s.peek()
    else:
        break


            