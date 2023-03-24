def canadaWeather():
    print("")
    cold = int(input("What's the threshold for cold in Canada, in Celsius?: "))
    F = int(input("What is today's temperature, in Fahrenheit?: "))
    C = (F - 32) * 5 / 9 
    if C <= cold:
        print("It is cold in Canada, brrr!")
    elif C > cold:
        print("It is not cold in Canada.")

def zigzag(a,b,c):
    if a < b > c:
        return True
    elif a > b < c:
        return True
    else:
        return False

def swapper():
    num = int(input("Enter integer between 9 and 21: "))
    vector = []
    pairs = []

    for x in range(num):
        vector.append(x)
    
    print(f"Original vector: {vector}")

    for x in vector:
        first, second = x, x+1
        if x == vector[-1]:
            pairs.append(first)
        else:
            pairs.append(second)
            pairs.append(first)
            vector.remove(first)
    
    print(f"Swapped vector: {pairs}")


canadaWeather()

print()

print(f"zigzag 33, 10, 30: {zigzag(33,10,30)}")

print()

swapper()
