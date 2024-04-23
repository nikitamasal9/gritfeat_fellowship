class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        newnode = TreeNode(data)
        if self.root is None:
            self.root = newnode
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = newnode
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = newnode
                    return
                current = current.right
        
    def delete(self, data):
        current = self.root
        return self._delete_recursively(current, data)

    def _delete_recursively(self, current, data):
        if current is None:
            return current

        if data < current.data:
            current.left = self._delete_recursively(current.left, data)
        elif data > current.data:
            current.right = self._delete_recursively(current.right, data)
        else:
            # Node with only one child or no child
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp
            node = current.right
            while node.left:
                node = node.left
            current.data = node.data
            current.right = self._delete_recursively(current.right, node.data)
        return current  


    
    def search(self, data):
        if self.root is None:
            print("Tree is empty")
            return False
        current = self.root
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False
    
    def inorder_traversal(self):
        result = []
        stack = []
        current = self.root

        while stack or current:
            while current:
               stack.append(current)
               current = current.left
            current = stack.pop()
            result.append(current.data)
            current = current.right
        return result
            
    
    def preorder_traversal(self):
    
        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(node.data)

            # Push the right child first so that it's processed after the left child
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result

    
    def postorder_traversal(self):
        result = []
        stack1 = [self.root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            result.append(stack2.pop().data)
        return result


# Example usage:
bst = BinarySearchTree()
arr = [21, 30, 25, 10, 12, 100, 5, 7, 3]
for i in arr:
    bst.insert(i)

print("Inorder traversal:", bst.inorder_traversal())
print("preorder traversal:", bst.preorder_traversal())
print("postorder traversal:", bst.postorder_traversal())

bst.delete(5)
print("After deleting 5:", bst.inorder_traversal())

print("Is 10 in the tree?", bst.search(10))
print("Is 6 in the tree?", bst.search(6))

print("Preorder traversal:", bst.preorder_traversal())

print("Postorder traversal:", bst.postorder_traversal())
