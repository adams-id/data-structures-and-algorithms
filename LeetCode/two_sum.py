"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Create a hashmap
        #Iterate through the nums array and store each element's value as the key and each element's index as the value in the hash table
        #Run another iteration that checks if he subtraction of each key in the hash map exists in tge map then return the index
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hashmap and hashmap[pair] != i:
                return [i, hashmap[pair]]
            
#   Time complexity O(n), Space Complexity = O(n)

# Explanation
"""
Intuition -

To improve our runtime complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to get its index. 
What is the best way to maintain a mapping of each element in the array to its index? A hash table.
We can reduce the lookup time from O(n) to O(1) by trading space for speed.
A hash table is well suited for this purpose because it supports fast lookup in near constant time.
I say "near" because if a collision occurred, a lookup could degenerate to O(n) time.
However, lookup in a hash table should be amortized O(1) time as long as the hash function was chosen carefully.

Algorithm

A simple implementation uses two iterations. In the first iteration, we add each element's value as a key and its index as a value to the hash table.
Then, in the second iteration, we check if each element's complement (target − nums[i]) exists in the hash table. 
If it does exist, we return current element's index and its complement's index. Beware that the complement must not be nums[i] itself!
"""

