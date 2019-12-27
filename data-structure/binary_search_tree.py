class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self, data=None):
        self.root = None
        if data:
            self.root = TreeNode(data)

    def insert(self, data):
        current = self.root  # a pointer to the current node
        parent = None  # suppose, the parent of the new node is None
        while current:
            parent = current  # update the parent
            if data > current.data:
                current = current.right
            else:
                current = current.left
        if self.root is None:
            self.root = TreeNode(data)
        elif data > parent.data:
            parent.right = TreeNode(data)
        else:
            parent.left = TreeNode(data)

    def inorder(self, current):
        if current is None:
            return
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)

    def print_inorder(self):
        self.inorder(self.root)

btree = BinaryTree(1)
btree.insert(7)
btree.insert(3)
btree.insert(4)
btree.insert(5)

btree.print_inorder()
