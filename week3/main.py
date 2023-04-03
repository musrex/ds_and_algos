from binSearchTree import *
from graph import *

def main():
    #filename = input("Enter filename: ")
    #data = open(filename, "r")
    data = open("numbers.txt", "r")
    numbers = Tree()
    for line in data:
        line = line.split()
        for x in line:
            numbers.insert(int(x))
    # numbers.printInorder()
    numbers.printPreorder()
    # numbers.printPostorder()
    print('-----')

    # result = numbers.inOrder()
    result = numbers.preOrder()
    # result = numbers.postOrder()

    matrix = [[0]*len(result) for i in range(len(result))]
    for x in range(len(result)-1):
        if result[x] > result[x+1]:
            weight = result[x] - result[x+1]
        else:
            weight = result[x+1] - result[x]
        if x not in matrix:
            matrix.append(weight)
    
    print(f'''matrix = {matrix[0]}
         {matrix[1]}
         {matrix[2]}
         {matrix[3]}
         {matrix[4]}
         {matrix[5:]}''')


if __name__ == "__main__":
    main()