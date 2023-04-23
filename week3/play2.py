class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
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

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

    def add_edge(self, i, j, weight):
        self.adj_matrix[i][j] = weight
        self.adj_matrix[j][i] = weight

    def __str__(self):
        output = []
        for i in range(1, self.n+1):
            output.append(' '.join([str(val) for val in self.adj_matrix[i][1:]]))
            output.append('\n')
        return ''.join(output)

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, "r") as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers

# Create a binary search tree and insert numbers from file
bst = BinarySearchTree()
numbers = read_numbers_from_file("numbers.txt")
for number in numbers:
    bst.insert(number)

# Calculate differences between nodes and create graph
differences = bst.calculate_differences()
n = len(numbers)
graph = Graph(n)
for i in range(1, n+1):
    for j in range(i+1, n+1):
        weight = abs(numbers[i-1] - numbers[j-1])
        graph.add_edge(i, j, weight)

# Print the differences and the graph
print("Differences between nodes:", differences)
print("Graph (adjacency matrix):\n", graph)