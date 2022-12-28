#1. Create an array and traverse.
#2. Access individual elements through indexes
#3. Append any value to the array using append() method
#4. Insert value in an array using insert() method
#5. Extend python array using extend() method
#6. Add items from list into array using fromlist() method 
#7. Remove any array element using remove() method 
#8. Remove last array element using pop() method
#9. Fetch any element through its index using index() method
#10. Reverse a python array using reverse() method
#11. Get array buffer information through buffer_info() method
#12. Check for number of occurrences of an element using count()
#13. Convert array to string using tostring() method
#14. Convert array to a python list with same elements using toli
#15. Append a string to char array using fromstring() method
#16. Slice Elements from an array


from array import *

#1.
arr = array('i', [2,6,8,9,13,23,56])
def traverseArray(array):
    for i in array:             # ------ Time complexity of this line = O(n)
        print("Question 1", i)
#traverseArray(arr)
#Time complexity - O(N)
#Space Complexity - O(N) since we are creating an array


#2.
print("Question 2", arr[1])       # ------ Time complexity of this line = O(1)
#Time complexity - O(1)
#Space Complexity - O(1)


#3.
arr.append(75)      # ------ Time complexity of this line = O(1)
print("Question 3", arr)
#Time complexity - O(1)
#Space Complexity - O(1)


#4.
arr.insert(5, 16)      # ------ Time complexity of this line = O(n)
print("Question 4", arr)
#Time complexity - O(N)
#Space Complexity - O(1)


#5.
arr2 = array("i", [100,110,120])
arr.extend(arr2)
print("Question 5", arr)


#6.
tempList = [125,130,135]
arr.fromlist(tempList)
print("Question 6", arr)


#7.
arr.remove(130)             # ------ Time complexity of this line = O(n)
print("Question 7", arr)
#Time complexity - O(N)
#Space Complexity - O(1)


#8.
arr.pop()             # ------ Time complexity of this line = O(1)
print("Question 8", arr)
#Time complexity - O(1)
#Space Complexity - O(1)


#9.
print("Question 9", arr.index(75))


#10.
arr.reverse()
print("Question 10", arr)


#11.
print("Question 11", arr.buffer_info())


#12.
arr.append(13)
print("Question 12", arr.count(13))


#14.
listTemp = arr.tolist()
print("Question 14", listTemp)


#14.
listTemp = arr.tolist()
print("Question 14", listTemp)


#16.
print("Question 16", arr[1:5])