class TreeNode:
    def __init__(self, data):
        # Set node value
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def treeSize(self, node):
        if node is not None:
            # (number of left subtree nodes) + 
            # (number of right subtree nodes) + 1 for current node
            return self.treeSize(node.left) + self.treeSize(node.right) + 1
        else:
            return 0

# Creating the binary tree
tree = BinaryTree()
tree.root = TreeNode(5)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(4)
tree.root.right.right = TreeNode(3)
tree.root.right.left = TreeNode(6)
tree.root.left.left = TreeNode(7)
tree.root.left.left.right = TreeNode(-3)

# Count number of nodes
size = tree.treeSize(tree.root)
print("Tree Size:", size)
