# 1) a) A 'decrease-by-a constant amount' algorithm
#       Mean of an array
def mean(A, n):
    '''
    input:  A: an array of numbers 
            n: an integer indicating how many of the array values
            need to be included in the calculations
    output: Calculated value of the mean
    '''
    if n == 1:
        return A[0]
    elif n > 1:
        return (n-1)/n * mean(A, n-1) + (1/n) * A[n-1]

# b)
A1 = [12, 23, 37, 45, 63, 82, 47, 75, 91, 88, 102]
A2 = [-1.7, 6.5, 8.2, 0.0, 4.7, 6.3, 9.5, 12.2, 37.9, 53.2]

result = mean(A1, 11) # 60.454545
result2 = mean(A2, 10) # 13.68
print(result)
print(result2)


# 2) a) A 'decrease-by-a constant factor' algorithm
#       Binary search
import math

def binarySearch(A, l, r, k):
    '''
    input: A: an array
           l: left subscript
           r: right subscript
           searchkey: what we're looking for in the array
    output: subscript where the searchkey is found
    '''
    m = math.floor((l + r) / 2)
    if r < l:
        return None
    else:
        print(m)
        if A[m] == k:
            return m
        elif A[m] < k:
            return binarySearch(A, l, m-1, k)
        else:
            return binarySearch(A, m+1, r, k)

A = [50, 41, 27, 20, 17, 12, 5]
A3 = [100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18] # l=0, r=14
binarySearch(A, 0, 6, 27)
result3=binarySearch(A3,0,14,87)
result4=binarySearch(A3,0,14,48)
result5=binarySearch(A3,0,14,33)
result6=binarySearch(A3,0,14,10)
print(f'''
search for 87 {result3}
search for 48 {result4}
search for 33 {result5}
search for 10 {result6}
''')


# 3) a) A 'decrease-by-a variable amount' algorithm
#       Euclidean Algorithm for Greatest Common Divisor(GCD)
def GCD():
    '''
    
    '''
    pass
