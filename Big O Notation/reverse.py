#	Question
# 	Find the runtime of the below code

def reverse(array):
    for i in range(0,int(len(array)/2)):    # ------ Time complexity of this line = O(N/2) = O(N)
        other = len(array)-i-1              # ------ Time complexity of this line = O(1)
        temp = array[i]                     # ------ Time complexity of this line = O(1)
        array[i] = array[other]             # ------ Time complexity of this line = O(1)
        array[other] = temp                 # ------ Time complexity of this line = O(1)
    print(array)                            # ------ Time complexity of this line = O(1)

#Summing up the time complexity of each line = O(N)