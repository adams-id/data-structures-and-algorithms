#Question
# Calculate the time complexity of the below block of code. The code finds the biggest number in an array

def findBiggestNumber(sampleArray):
  biggestNumber = sampleArray[0]           # ------ Time complexity of this line = O(1)
  for index in range(1, len(sampleArray)): # ------ Time complexity of this line = O(n)
    if sampleArray[index] > biggestNumber: # ------ Time complexity of this line = O(1)
      biggestNumber = sampleArray[index]   # ------ Time complexity of this line = O(1)
  print(biggestNumber)                     # ------ Time complexity of this line = O(1)

#Summing up the time complexity of each line = O(1) + O(n) + O(1) + O(1) + O(1) = O(n)