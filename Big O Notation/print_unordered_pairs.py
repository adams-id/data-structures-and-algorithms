#	Question
# 	Find the runtime of the three seperate codes below
#   1)
def printUnorderedPairs(array):
    for i in range(0,len(array)):      
        for j in range(i+1,len(array)):      
            print(array[i] + "," + array[j])    

# This is a nested for loop so the time complexity is O(N²)


#   2)
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):                    # ------ Time complexity of this line = O(a)
        for j in range(len(arrayB)):                # ------ Time complexity of this line = O(b)
            if arrayA[i] < arrayB[j]:               # ------ Time complexity of this line = O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j]))    # ------ Time complexity of this line = O(1)

arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]

# Since array a and array b is different, the loop is based on the length of each arrays.
# As per a nested for loop, we multiply the complexities giving us O(ab)


#   3)
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):                    # ------ Time complexity of this line = O(a)
        for j in range(len(arrayB)):                # ------ Time complexity of this line = O(b)
            for k in range(0,100000):               # ------ Time complexity of this line = O(100000) = O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j]))    # ------ Time complexity of this line = O(1)

# As per a nested for loop, we multiply the complexities giving us O(ab)
