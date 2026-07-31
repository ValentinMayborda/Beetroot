# Root
# Node
# Edge
# Parent
# Child
# Leaf
# Height
# Level
# Subtree

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))