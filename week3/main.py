from binSearchTree import *
from tree import *

def main():
    #filename = input("Enter filename: ")
    #data = open(filename, "r")
    data = open("numbers.txt", "r")
    numbers = Tree()
    for line in data:
        line = line.split()
        for x in line:
            numbers.insert(x)
    numbers.printInorder()
    numbers.printPreorder()
    numbers.printPostorder()
    result = numbers.check('g')
    print(result)
    print(numbers.getRoot())

# def main():


 #   pass






if __name__ == "__main__":
    main()