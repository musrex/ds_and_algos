class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if not current_node.left:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if not current_node.right:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        else:
            print("Value already exists in tree")

    def calculate_differences(self):
        differences = []
        if self.root:
            self._calculate_differences(self.root, differences)
        return differences

    def _calculate_differences(self, current_node, differences):
        if current_node.left:
            differences.append(current_node.value - current_node.left.value)
            self._calculate_differences(current_node.left, differences)
        if current_node.right:
            differences.append(current_node.right.value - current_node.value)
            self._calculate_differences(current_node.right, differences)