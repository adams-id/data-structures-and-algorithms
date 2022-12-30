#   Question 1: How to check if an array contains a number in python
#   Question 2: How to find the maximum product of two ntegers in the array where all elements are positive

import numpy as np 

#Solution 1
def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print("The number exists at index " + str(i))
            break

#Time complexity is O(N)

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
findNumber(myArray, 15)

#Solution 2
def maxProduct(array):
    product = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j] > product:
                product = array[i]*array[j]
                pairs = str(array[i])+ "," + str(array[j])
    print(pairs)
    print(product)

#Time complexity is O(N²)
maxProduct(myArray)