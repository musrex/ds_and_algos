from person import *

s = []

data = open("Lopez_Family_Farm.csv", "r")

def readKids(filename):
    data = open(filename,"r")
    kids = {}
    for line in data:
        line = line.split(',')
        kids.update({line[0]:person(line[1],line[2],int(line[3]))})
        for k in kids:
            if k not in s:
                s.append(k)
    return kids
    # print("============================")
    # print("  Nickname  Name            ")
    # print("============================")
    # print(s)
    # for k in kids:
        # print("{0:>10}  {1:<15}".format(k,kids[k].getFullName()))

def main():
    #filename = input("Enter filename: ")
    readKids("Lopez_Family_Farm.csv")
    run = True
    while run:
        toRemove = input("Enter the number (1-4) of items to remove: ")
        try:
            toRemove = int(toRemove)
            for num in range(toRemove):
                s.pop()
            # NEEDS WORK
            #for k in kids:
            #    if s[-1] == k:
            #        print(k)
        except:
            input("Please enter a number in the range of 1-4. Press Enter to continue.")
main()