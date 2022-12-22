#	Question
# 	Find the runtime of the below code

def printPairs(array):
    for i in array:						# ------ Time complexity of this line = O(n²)
        for j in array:					# ------ Time complexity of this line = O(n)
            print(str(i)+","+str(j))	# ------ Time complexity of this line = O(1)

# This is a nested for loop so the time complexity is O(N²)