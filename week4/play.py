# 1) Find the number of entries in an array of integers that are divisible by a given integer. Your function
# should have two input parameters – an array of integers and a positive integer – and should return an
# integer indicating the count using a return statement.
# Run your algorithm on the problem instances:

a = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65 ] # number = 3
b = [18, 45, 77, 81, 33, 54, 99] # number = 9

# input - an ARRAY to iterate through, and the NUMBER we are dividing by
# ouput - a counter variable that gets incremented everytime an int in the array is divisible by input NUMBER
def howMany(array, number):
    count = 0

    # in this for loop check to see if the int in the array is divisible by our number 
    # and if so we iterate the counter
    for i in array:
        if i % number == 0:
            count += 1

    return count

result = howMany(a, 3) # result is 3
result2 = howMany(b, 9) # result is 5



# 2) Given an array of real numbers, without sorting the array, find the smallest gap between all pairs of elements 
# (for an array A, the absolute value of the difference between elements 𝐴[i] and 𝐴[𝑗]). Your function should have 
# one input parameter – an array of numbers – and should return a non-negative number indicating the smallest gap using a return statement.
# Run your algorithm on the problem instances:

a = [50, 120, 250, 100, 20, 300, 200]
b = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]

# input - array
# output - a pair of values from the array with the smallest difference between them
def smallestGap(array):
    # if the length our array is less than 2, we can’t return a pair so we return None
    n = len(array)
    if n < 2:
        return None

    # initialize min_gap and pair variables, if these first two are our smallest pair, great
    # if they're not, the for loop that follows assigns the new smallest pair
    min_gap = abs(array[0]-array[1])
    pair = (array[0]-array[1])

    # in this for loop we iterate through out range (defined by length of array)
    # and then we iterate through a range that excludes the first value we'll compare, 'i'
    for i in range(n):
        for j in range(i+1,n):
            # we define gap, and if gap is smaller than min_gap, we declare gap to be min_gap
            # and assign the variables with the min_gap as the pair to be returned
            gap = abs(array[i]-array[j])
            if gap < min_gap:
                min_gap = gap
                pair = (array[i], array[j])

    return(pair)

result1 = smallestGap(a) # result is (120, 100)
result2 = smallestGap(b) # result is (8.1, 5.09)



#3) Given an integer n>=2 and two nxn matrices A and B of real numbers, find the product AB of the matrices. 
# Your function should have three input parameters – a positive integer n and two nxn 
# matrices of numbers– and should return the nxn product matrix using a return statement.
# Run your algorithm on the problem instances: 
n = 2
a = [[2, 7],
     [3, 5],]

b = [[8, -4],
     [6, 6]]

n2 = 3
a2 = [[1,0,3],
     [3, -2, 5],
     [6, 2, -3]]

b2 = [[0.3, 0.25, 0.1],
     [0.4, 0.8, 0],
     [-0.5, 0.75, 0.6]]

# input - n (the size of our matrix), A & B - the matrices we are multiplying
# output - the matrix that results from multiplying matrix A & B
def matrix_multiply(n, A, B):
    # we create our matrix, and initialize all entries to 0
    AB = [[0 for j in range(n)] for i in range(n)]

    # we iterate through the rows and columns of AB
    # as well as the rows anc columns of A and B, 
    # adding the results of the computations to AB
    for i in range(n):
        for j in range(n):
            for k in range(n):
                AB[i][j] += A[i][k] * B[k][j]
    return AB

result = matrix_multiply(n, a, b)       #result is [[58, 34], [54, 18]]
result2 = matrix_multiply(n2, a2, b2)   #result is [[-1.2, 2.5, 1.9], [-2.4000000000000004, 2.9, 3.3], [4.1, 0.8500000000000001, -1.1999999999999997]]