class Node:
    ''' 
    A class to represent a single node in a linked list.
    '''
    def __init__(self, data: int):
        self.data = data
        self.next = None

class Chaining(Node):
    '''
    A class to implement hashing using chaining method.
    '''
    def __init__(self, slots):
        '''
        Initializing the Chaining object.

        Args:
            slots(int): The size of the array of linked lists.
        '''
        self.slots = slots
        self.chain = [None] * self.slots
        self.elements = 0

    def hashFxn(self, data):
        '''
          Returning the hash value of the data to search
        '''
        return data % self.slots

    def append(self, data: int) -> None:
        """
        Inserts an element into the appropriate slot based on hash value.

        Parameters
        ----------
        data : int
        """
        new_node = Node(data)
        index = self.hashFxn(data)
        if self.chain[index] is None:
            self.chain[index] = new_node
        else:
          # if collision occurs
          new_node.next = self.chain[index]
          self.chain[index] = new_node
        self.elements += 1

    def __delitem__(self, data: int) -> None:
        """
        Deletes an element from the appropriate slot based on hash value.

        Parameters
        ----------
        data : int
        """
        index = self.hashFxn(data)
        current = self.chain[index]
        prev = None

        while current is not None:
            if current.data  == data:
                if prev is None:
                    self.chain[index] = current.next
                else:
                    prev.next = current.next
                self.elements -= 1
                print(f"{data} has been deleted.")
                return
            prev = current
            current = current.next

        print("The required element does not exist")


    def __getitem__(self, data: int) -> int:
        """
        Search for an element and returns its value

        Parameters
        ----------
        data : int
            Element to be searched

        Returns
        -------
        int
            Element searched
        """
        index = self.hashFxn(data)
        current = self.chain[index]
        while current is not None:
            if current.data == data:
                return current.data
            current = current.next
        return "Element not found"

    def __len__(self):
        """ Returns the number of elements in the hash table. """
        return self.elements

    def __str__(self):
        # """ Display the contents of the hash table """
        # for i, j in enumerate(self.chain):
        #     print(f"Slot {i}: ", end=" ")
        #     current = j # address to the node in the bucket
        #     while current is not None:
        #         print(current.data, end=" -> " if current.next else "")
        #         current = current.next
        #     print()
        """ Return a string representation of the hash table """
        string = ""
        for i, j in enumerate(self.chain):
            string += f"Slot {i}: "
            current = j
            while current is not None:
                string += str(current.data)
                if current.next:
                    string += " -> "
                current = current.next
            string += "\n"
        return string
    
obj = Chaining(5) # Create an object of class chain with 5 slots

# Inserting elements into the obj
obj.append(2)
obj.append(5)
obj.append(3)
obj.append(10)
obj.append(15)
obj.append(22)
obj.append(46)
obj.append(11)
obj.append(73)

print(obj) # Display the elements in the obj

del obj[10] # deleting an element
print(obj)

obj[73] # search an element in the obj
obj[90]

del obj[1]

len(obj)

