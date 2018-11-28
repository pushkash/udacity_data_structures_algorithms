class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.internal_insert(self.root, new_val)

    def internal_insert(self, current_node, new_val):
        if new_val < current_node.value:
            if current_node.left:
                self.internal_insert(current_node.left, new_val)
            else:
                current_node.left = Node(new_val)
        elif new_val > current_node.value:
            if current_node.right:
                self.internal_insert(current_node.right, new_val)
            else:
                current_node.right = Node(new_val)


    def search(self, find_val):
        tmp = self.root

        while tmp:

            if tmp.value == find_val:
                return True

            if find_val < tmp.value:
                if tmp.left:
                    tmp = tmp.left
                else:
                    return False

            elif find_val > tmp.value:
                if tmp.right:
                    tmp = tmp.right
                else:
                    return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(10)


# Check search
# Should be True
print tree.search(2)
# # Should be False
print tree.search(6)
print tree.search(10)