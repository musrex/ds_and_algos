from main import *

def main():
      
    data = open("data.txt", "r")
    x = 0
    a = []
    L = LinkedList()
    count = 0
    
    # read through the lines of the file, strip trailing characters and append the data to our file.
    # We also use a counter so that we know how many values to iterate through
    for line in data:
        line = line.rstrip()
        a.append(line)
        count += 1

    a.sort()

    # we insert num next to the current, then move current over to num so that our linked list remains sorted
    for num in a:
        L.insertCurrentNext(int(num))
        L.nextCurrent()

    L.resetCurrent()
    L.display()
    x = input("Enter integer value: ")
    x = int(x)

    # we start a while loop so we can iterate through the linked list
    run = True
    while run:
        # this condition checks to see if it's the last item in the list, and adds x at the end
        if L.Current.Next is None:
            L.insertCurrentNext(x)
            run = False
            break
        # this condition checks to see if the first element is equal to x, and if so removes it
        elif L.getCurrent() == x:
            L.removeBeginning()
            run = False
            break
        # this condition checks to see if the next element is equal to x, and if so removes it
        elif L.Current.Next.Data == x:
            L.removeCurrentNext()
            run = False
            break
        # this condition checks to see if the first item is larger than x, and if so adds x to the front
        elif L.getCurrent() > x:
            L.insertBeginning(x)
            run = False
            break
        # this condition checks to see if the next item is larger than x, and if so adds x next (or in other words, in front of next)
        elif int(L.Current.Next.Data) > x:
            L.insertCurrentNext(x)
            run = False
            break
        # this condition allows us to traverse the list
        else: 
            L.nextCurrent()

    L.display()


main()

