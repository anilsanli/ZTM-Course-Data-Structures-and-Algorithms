class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if current_node.value > value:
                    # Left
                    if current_node.left is None:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                else:
                    # Right
                    if current_node.right is None:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

    def lookup(self, value):
        pass

    def remove(self, value):
        pass

def traverse(node):
    tree = {"value": node.value}
    tree["left"] = None if node.left is None else traverse(node.left)
    tree["right"] = None if node.right is None else traverse(node.right)
    return tree

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.remove(170)
print(traverse(tree.root))
# {'value': 9, 'left': {'value': 4, 'left': {'value': 1, 'left': None, 'right': None}, 'right': {'value': 6, 'left': None, 'right': None}}, 'right': {'value': 20, 'left': {'value': 15, 'left': None, 'right': None}, 'right': None}}
