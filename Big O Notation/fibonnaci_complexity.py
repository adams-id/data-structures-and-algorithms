#	Question
# 	Find the runtime of the below code

def allFib(n):
    for i in range(n):                      # ------ Time complexity of this line which is gotten from the below line = O(N)
        print(str(i)+":, " + str(fib(i)))   # ------ Time complexity of this line which is gotten from the below line = O(2^N)

def fib(n):
    if n <= 0:                      # ------ Time complexity of this line = O(1)
        return 0                    # ------ Time complexity of this line = O(1)
    elif n == 1:                    # ------ Time complexity of this line = O(1)
        return 1                    # ------ Time complexity of this line = O(1)
    return fib(n-1) + fib(n-2)      # ------ Time complexity of this line = O(branches^N) where branches is 2 cos it calls itself twice = O(2^N)

allFib(4)

#Summing up the time complexity of each line = O(2^N)