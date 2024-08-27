class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

def in_order_traversal(node):
    if not node:
        return []
    result = []
    if node:
        result.extend(in_order_traversal(node.left))
        result.append(node.value)
        result.extend(in_order_traversal(node.right))
    return result

def pre_order(root):
    if not root:
        return []

    result = [root.value]
    result.extend(pre_order(root.left))
    result.extend(pre_order(root.right))

    return result

def post_order(root):
    if not root:
        return []

    result = []
    result.extend(post_order(root.right))
    result.extend(post_order(root.left))
    result.append(root.value)

    return result


def insert(node, value):
    if not node:
        return Node(value)

    if node.value == value:
        return None

    elif value > node.value:
        node.right = insert(node.right, value)

    else:
        node.left = insert(node.left, value)

    return node

def delete(node, value):
    if not node:
        return None
    
    if value < node.value:
        node.left = delete(node.left, value)

    elif value > node.value:
        node.right = delete(node.right, value)

    else:
        if not node.left and not node.right:
            node = None

        elif node.left is None:
            node = node.right

        elif node.right is None:
            node = node.left

        else:
            succesor = find_succesor(node.right)
            node.value = successor.value
            node.right = insert(node.right, succesor.value)

def find_successor(node):
    while node and node.left:
        node = node.left
    return node

