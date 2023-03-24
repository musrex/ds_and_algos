from linkedlist import *
#from main import *

data = open("data.txt", "r")
x = 0
a = []
L = LinkedList()
for line in data:
    line = line.rstrip()
    a.append(line)
    x += 1
    print(f"{x}: {line}")

a.sort()
for num in a:
    L.add(int(num))

print(a)
L.display()
print(f"Linked List size: {L.get_size()}")

x = input("Enter integer value: ")
x = int(x)

if L.find(x):
    L.remove(x)
else:
    L.add(x)

L.display()
print(f"Linked List size: {L.get_size()}")