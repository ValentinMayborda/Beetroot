# BST

# Клас вузла
class Node:
    def __init__(self, value):
        self.value = value  # Значення вузла
        self.left = None    # Ліва дитина (всі менші значення)
        self.right = None   # Права дитина (всі більші значення)



class BinarySearchTree:
    def __init__(self):
        self.root = None  # Корінь дерева

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:       # Значення менше - йдемо ліворуч
                if current.left is None:    # Лівого вузла немає - вставляємо тут
                    current.left = Node(value)
                    break
                current = current.left      # Інакше переходимо ліворуч
            else:  # Значення більше або рівне - йдемо праворуч
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right

    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def get_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def get_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self, node):
        if not node:
            return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return abs(left_height - right_height) <= 1 and self.is_balanced(node.left) and self.is_balanced(node.right)

    def delete(self, value):
        def _delete(node, val):
            if not node:
                return None
            if val < node.value:
                node.left = _delete(node.left, val)
            elif val > node.value:
                node.right = _delete(node.right, val)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.value = successor.value
                node.right = _delete(node.right, successor.value)
            return node
        self.root = _delete(self.root, value)


def inorder(node, result=[]):
    """Ліво -> Корінь -> Право"""
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)
    return result

def preorder(node, result=[]):
    """Корінь -> Ліво -> Право"""
    if node:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)
    return result

def postorder(node, result=[]):
    """Ліво -> Право -> Корінь"""
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)
    return result

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print(bst.search(20))
print(bst.get_min())
print(bst.get_max())

print(bst.height(bst.root))
print(bst.is_balanced(bst.root))

bst.delete(30)
print(bst.get_min())
inorder_result = inorder(bst.root)
print(f"Inorder: {inorder_result}")
preorder_result = preorder(bst.root)
print(f"Preorder: {preorder_result}")
postorder_result = postorder(bst.root)
print(f"Postorder: {postorder_result}")