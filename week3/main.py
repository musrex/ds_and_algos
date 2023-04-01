from binSearchTree import *
from tree import *

def main():
    filename = input("Enter filename: ")
    data = open(filename, "r")
    numbers = Tree()
    for line in data:
        line = line.split()
        numbers.insert(line)
    numbers.printInorder()

#def main():


 #   pass






if __name__ == "__main__":
    main()