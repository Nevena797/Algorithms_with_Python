class Treenode:
    def __init__(self, element=None, parent=None, right=None, left=None):
        self.element = element
        self.parent_node = parent
        self.right_node = right
        self.left_node = left


# search - iterative n(logn)
def find(key, n):
    while n != None and n.key != key:
        if key < n.key:
            n = n.left
        else:
            n = n.right
    return n


# recursive

def find(key, node):
    if node is None:
        print("Reached None → element not found")
        return None

    print(f"Currently at node: {node.element}")

    if node.element == key:
        print(f"Found {key} ✅")
        return node

    if key < node.element:
        print(f"{key} < {node.element} → going left")
        return find(key, node.left_node)

    print(f"{key} > {node.element} → going right")
    return find(key, node.right_node)

# root
root = Treenode(10)

# left subtree
node5 = Treenode(5, parent=root)
node2 = Treenode(2, parent=node5)
node7 = Treenode(7, parent=node5)

# right subtree
node15 = Treenode(15, parent=root)
node20 = Treenode(20, parent=node15)

# linking
root.left_node = node5
root.right_node = node15

node5.left_node = node2
node5.right_node = node7

node15.right_node = node20

find(7, root)