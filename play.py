import math

#for x in range(1, 11):
#    print(x,": ", math.factorial(x))
    
num = 0
for x in range(1, 8):  
    x = 2**-x
    num = num + x

print(num)
