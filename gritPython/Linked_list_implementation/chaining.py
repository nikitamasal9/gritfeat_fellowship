class Node:
    '''
    Implementing linked list node.
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table implementation using chaining for collision resolution.
    '''

    def __init__(self, size):
        '''
        Initializing the hash table with a specified size.

        Args:
        size (int): The size of the hash table.
        '''
        self.size = size
        self.table = [None] * size

    
    def __hash__(self, key):
        '''
        Returning the hash value.
        '''
        return len(key) % self.size

    def __getitem__(self, key):
        '''
        (searching)Getting the value associated with the given key using square bracket notation.

        Args:
            key: The key to be searched.

        Returns:
            The value associated with the key, or None if the key is not found.
        '''
        index = self.__hash__(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def __setitem__(self, key, value):
        '''
        (Inserting)Setting the value associated with the given key.

        Args:
            key: The key to be inserted.
            value: The value associated with the key.
        '''
        index = self.__hash__(key)
        node = self.table[index]
        if not node:
             self.table[index] = Node(key, value)
        else:
            while node.next:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = Node(key, value)
       

    def __delitem__(self, key):
        '''
        Deleting the key-value pair associated with the given key.

        Args:
        key: The key to be removed.
        '''
        index = self.__hash__(key)
        node = self.table[index]
        if not node:
            raise KeyError(f"Key '{key}' not found")
        elif node.key == key:
            self.table[index] = node.next
        else:
            while node.next:
                if node.next.key == key:
                    node.next = node.next.next
                    return
                node = node.next
            raise KeyError(f"Key '{key}' not found")
    
    def __len__(self):
        '''
        Returns the total number of elements in the hash table.

        Returns:
            int: The total number of elements in the hash table.
        '''
        total_elements = 0
        for node in self.table:
            while node:
                total_elements += 1
                node = node.next
        return total_elements

    def __str__(self):
        '''
        Returns a string representation of the hash table.

        Returns:
            str: String representation of the hash table.
        '''
        table_str = ""
        for i, node in enumerate(self.table):
            table_str += f"Bucket {i}: "
            while node:
                table_str += f"({node.key}, {node.value}) ->"
                node = node.next
            table_str += "None \n"
        return table_str


# Testing:
hash_table = HashTable(10)
hash_table["bhatbhateni"] = 5
hash_table["bigmart"] = 7
hash_table["nina&hager"] = 9
hash_table["miniso"] = 4
hash_table["yoyoso"] = 9
print(hash_table)

print("Value for 'bhatbhateni':", hash_table["bhatbhateni"])
print("Value for 'bigmart':", hash_table["bigmart"])
print("Value for 'nina&hager':", hash_table["nina&hager"])
print("Value for 'miniso':", hash_table["miniso"])
print("Value for 'yoyoso':", hash_table["yoyoso"])

print("Length of hash table:", len(hash_table))

del hash_table["yoyoso"]
print("After removing 'yoyoso':")
print(hash_table)

print("Length of hash table after removing:", len(hash_table))
