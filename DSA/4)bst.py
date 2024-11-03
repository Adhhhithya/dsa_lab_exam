class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(root, newValue):
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        root.rightChild = insert(root.rightChild, newValue)
    return root

def search(root, value):
    if root is None:
        return False
    elif root.data == value:
        return True
    elif root.data > value:
        return search(root.leftChild, value)
    else:
        return search(root.rightChild, value)

# Creating the binary search tree
root = insert(None, 50)
insert(root, 20)
insert(root, 53)
insert(root, 11)
insert(root, 22)
insert(root, 52)
insert(root, 78)

# Accessing nodes for display purposes
node1 = root
node2 = node1.leftChild
node3 = node1.rightChild
node4 = node2.leftChild
node5 = node2.rightChild
node6 = node3.leftChild
node7 = node3.rightChild

# Printing nodes and their children
print("Root Node is:")
print(node1.data)
print("Left child of the root node is:")
print(node1.leftChild.data)
print("Right child of the root node is:")
print(node1.rightChild.data)

print("\nNode is:", node2.data)
print("Left child of the node is:", node2.leftChild.data)
print("Right child of the node is:", node2.rightChild.data)

print("\nNode is:", node3.data)
print("Left child of the node is:", node3.leftChild.data)
print("Right child of the node is:", node3.rightChild.data)

print("\nNode is:", node4.data)
print("Left child of the node is:", node4.leftChild)
print("Right child of the node is:", node4.rightChild)

print("\nNode is:", node5.data)
print("Left child of the node is:", node5.leftChild)
print("Right child of the node is:", node5.rightChild)

print("\nNode is:", node6.data)
print("Left child of the node is:", node6.leftChild)
print("Right child of the node is:", node6.rightChild)

print("\nNode is:", node7.data)
print("Left child of the node is:", node7.leftChild)
print("Right child of the node is:", node7.rightChild)

# Searching for elements in the binary search tree
print("\nSearching for elements in the tree:")
print("53 is present in the binary tree:", search(root, 53))
print("100 is present in the binary tree:", search(root, 100))
