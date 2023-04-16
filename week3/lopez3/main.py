from binSearchTree import *
from graph import *

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, "r") as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers

def main():
    # Create a binary search tree and insert numbers from file
    tree = Tree()
    numbers = read_numbers_from_file("numbers.txt")
    for number in numbers:
        tree.insert(number)
    
    # Calculate differences between nodes and create graph
    differences = tree.calculate_differences()
    n = len(numbers)
    graph = Graph(n)
    for i in range(n):
        for j in range(i+1, n):
            weight = abs(numbers[i] - numbers[j])
            graph.add_edge(i, j, weight)
    
    # Print the differences and the graph
    print("Differences between nodes:", differences)
    print("Matrix:\n", graph)



if __name__ == "__main__":
    main()
