#   Question - Contains Duplicate

""" 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

#   Solution
def isUnique(nums):
    newList = []
    for i in range(len(nums)):
        if nums[i] in newList:
            print( ("true"))
            return True
        else:
            newList.append(nums[i])
    print("false")
    return False

myList = [11, 20, 30, 44, 5, 56, 57, 8, 11, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]
isUnique(myList)