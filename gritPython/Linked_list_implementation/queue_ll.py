class Node:
    def __init__(self, data):
        '''
        Initializing a Node object with the given data.

        Args:
            data: The data to be stored in the node.
        '''
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        '''
        Initializing an empty Queue.
        '''
        self.front = None
        self.rear = None

    def isempty(self):
        '''
        Checks if the queue is empty.
        '''
        if self.front == None:
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def enqueue(self):
        '''
        Inserting an element into the rear of the queue.
        '''
        x = int(input("Enter data to be inserted into the queue: "))
        new = Node(x)
        if self.front is None:
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def dequeue(self):
        '''
        Removing an element from the front of the queue.
        '''
        if self.front is None:
            print("Queue is empty.")
        elif self.front.next is None:
            print("Deleted elemnt is: ", self.front.data)
            self.front = None
        else:
            temp = self.front
            print("Deleted element is:", self.front.data)
            self.front = temp.next
            temp = None

    def display(self):
        '''
        Displaying all the elements in the queue.
        '''
        if self.front is None:
            print("Queue is empty")
        else:
            print("Element in queue : ")
            temp = self.front
            while temp:
                print(temp.data)
                temp = temp.next

    def peek(self):
        '''
        Displaying the element at the front of the queue without removing it.
        '''
        if self.front is None:
            print("Queue is empty")
        else:
            print("Element on the top of the queue: ", self.front.data)


#Testing:
q = Queue()
while(1):
    print("Enter the options from below")
    print("1-Enqueue operation \n 2-Dequeue operation \n 3-IsEmpty operation \n 4-Display \n 5-Peek operation \n 6-Exit")
    option = int(input())
    if option == 1:
        print("Enqueue operation")
        q.enqueue()
    elif option == 2:
        print("Dequeue operation")
        q.dequeue()
    elif option == 3:
        print("IsEmpty operation")
        q.isempty()
    elif option == 4:
        print("Display")
        q.display()
    elif option == 5:
        print("Peek operation")
        q.peek()
    else:
        break
