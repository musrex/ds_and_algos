A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]


# Input: An array A and indices i and j.
# Output: An array where A[i] and A[j] have been swapped.
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def SelectionSort(A):
    for i in range(len(A)-1, 0, -1):
        m = i
        comparisons = 0
        swaps = 0

        for j in range(0, i):
            comparisons += 1
            if A[j] > A[m]:
                m = j

        if m != i:
            Swap(A, i, m)
            swaps += 1

        print(f'''Iteration {len(A) - i}: {A} 
Comparisons: {comparisons} 
Swaps: {swaps}''')
print("\n***************Result 1****************")
result1 = SelectionSort(A1)
print("=======================================")
print("\n***************Result 2****************")
result2 = SelectionSort(A2)
print("=======================================")
print("\n***************Result 3****************")
result3 = SelectionSort(A3)
print("=======================================")

A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

# Input: An array A of integers.
# Output: An array A sorted in increasing order.
def BubbleSort(A):
    total_comparisons = 0
    total_swaps = 0

    for i in range(len(A) - 1):
        comparisons = 0
        swaps = 0

        for j in range(len(A) - i - 1):
            comparisons += 1
            if A[j + 1] < A[j]:
                Swap(A, j + 1, j)
                swaps += 1

        print(f'''Iteration {i + 1}: {A}
Comparisons: {comparisons}
Swaps: {swaps}''')

        total_comparisons += comparisons
        total_swaps += swaps

        if swaps == 0:
            break

    print(f'''Total Comparisons: {total_comparisons}
Total Swaps: {total_swaps}''')




print("\n***************Result 4****************")
result4 = BubbleSort(A4)
print("=======================================")
print("\n***************Result 5****************")
result5 = BubbleSort(A5)
print("=======================================")
print("\n***************Result 6****************")
result6 = BubbleSort(A6)
print("=======================================")




# 3 
# a
def power(x, p):
    sum = x
    for i in range(p-1):
        sum *= x
    return sum

result7 = power(2, 5)
print(result7)
print(2**5)

# b
A7 = [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9]
def evaluate(A, x):
    n = len(A)
    result = 0
    for i in range(n):
        result += A[i] * power(x, i)
    return result

# c
result8 = evaluate(A7, 5.4) # result 227295.86317440012
print(result8)        

# d
# The function uses a loop to iterate through each term,
# so the loop runs n + 1 times for a polynomial of n.
# Inside the loop, we call the power function of x raised
# to p power. 
# So the total number of multiplications is:
# 1 + 2 + 3 + ... + n + 1
# we can evaluate that to n(n+1)/2
# this can be further evaluated to (n+1)(n+2)/2
# this falls under the worst case classification O(n^2)

