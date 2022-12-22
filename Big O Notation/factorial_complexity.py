#	Question
# 	Find the runtime of the below code

def factorial(n):                        # ------ Time complexity of this line = M(n)
    if n < 0:                           # ------ Time complexity of this line = O(1)
        return -1                       # ------ Time complexity of this line = O(1)
    elif n == 0:                        # ------ Time complexity of this line = O(1)
        return 1                        # ------ Time complexity of this line = O(1)
    else:                               
        return n * factorial(n-1)       # ------ Time complexity of this line = M(n-1)

#Summing up the time complexity of each line = O(N)