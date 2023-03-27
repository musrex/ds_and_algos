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


def main():
    #filename = input("Enter filename: ")
    kids = readKids("Lopez_Family_Farm.csv")
    
    # start up a while loop so we can repeatedly prompt user
    run = True
    while run:
        print(s)
        # exit loop and quit program once stack is empty
        if len(s) == 0:
            print("No more names in the stack")
            run = False
            break
        else:
            # we take user input and then 
            toRemove = input("Enter the number (1-4) of items to remove: ")
            try:
                # in a try block conver
                toRemove = int(toRemove)
                if toRemove in range(1,5):
                    # we use the number of items as the input and end the program
                    if len(s) <= toRemove:
                        for num in range(len(s)):
                            s.pop()
                            #print("No more names in the stack")
                            #run = False
                            #break
                    # this gets the key from the top of the stack and uses it to retrieve our person object.
                    else:
                        for num in range(toRemove):
                            s.pop()
                    # if the user inputs a number higher than the number of items in the list
                        for k in kids:
                            if s[-1] == k:
                                print(f'''    {k},{kids[k].getFullName(),kids[k].getAge()}''')
                                print(f"Stack size: {len(s)}")
                else:
                    input("Please enter a number in the range of 1-4. Press Enter to continue.")
            except:
                input("Please enter a number in the range of 1-4. Press Enter to continue.")
main()