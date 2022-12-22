#	Question
# 	Find the runtime of the below code

def foo(array):
    sum = 0					# ------ Time complexity of this line = O(1)
    product = 1				# ------ Time complexity of this line = O(1)
    for i in array:			# ------ Time complexity of this line = O(n)
        sum += i			# ------ Time complexity of this line = O(1)
    for i in array:			# ------ Time complexity of this line = O(n)
        product *= i		# ------ Time complexity of this line = O(1)
    print("Sum = "+str(sum)+", Product = "+str(product))	# ------ Time complexity of this line = O(1)

ar1 = [1,2,3,4]
foo(ar1)

#Summing up the time complexity of each line = O(1) + O(1) + O(n) + O(1) + O(n) + O(1) + O(1) = O(N)