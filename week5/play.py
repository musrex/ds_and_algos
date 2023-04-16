A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]


# Input: An array A and indices i and j.
# Output: An array where A[i] and A[j] have been swapped.
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Input: An array A of integers.
# Output: Array A sorted in increasing order.
def SelectionSort(A):
    for i in range(len(A)-1):
        m = i
    
        # Find the smallest element in A[i...n-1]
        for j in range(i+1, len(A)):
            count = 0
            print(A)
            
            if A[j] > A[m]:
                count += 1
                m = j
        Swap(A, i, m)
        
    print(f'''{A}
{count}''')


result1 = SelectionSort(A1)
result2 = SelectionSort(A2)
result3 = SelectionSort(A3)
