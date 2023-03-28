from person import *

s = []

# this function reads our file and adds items from each line to a dictionary 
def readKids(filename):
    data = open(filename,"r")
    kids = {}
    for line in data:
        line = line.split(',')                                      # with these two lines we use .split and then [0] to set first name as Key then for the value
        kids.update({line[0]:person(line[1],line[2],int(line[3]))}) # we create an instance of the person class, passing the other indeces as class parameters 
        for k in kids:
            if k not in s:
                s.append(k)
    return kids


def main():
    filename = input("Enter filename: ")
    kids = readKids(filename)
    
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
                # in a try block (for easy error handling) convert it to an int
                toRemove = int(toRemove)
                if toRemove in range(1,5):      
                    if len(s) <= toRemove:          # if the size of the stack is less than or equal to the input, we use the stack size 
                        for num in range(len(s)):   # instead of input to avoid errors in removing 4 items when there might only be 3 or less
                            s.pop()
                    else:
                        for num in range(toRemove): # otherwise we just use the input to determine how many times we .pop()
                            s.pop()
                        # in the following for loop, we we match the last item in the list to k (key), if it matches we print that k and the object parameters
                        for k in kids:
                            if s[-1] == k:
                                print(k,kids[k].getFullName(),kids[k].getAge())
                                print(f"Stack size: {len(s)}")
                else:
                    input("Please enter a number in the range of 1-4. Press Enter to continue.")
            except:
                input("Please enter a number in the range of 1-4. Press Enter to continue.")
main()