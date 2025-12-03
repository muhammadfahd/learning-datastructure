'''
Leetcode Probblem 217 - Contain Duplicate


217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:
Input: nums = [1,2,3,1]
Output: true

Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


'''

# Approach 1 

def containsDuplicate(nums) -> bool:
    # 1. Sort the list so duplicates sit next to each other
    nums.sort()
    
    # 2. Check neighbors
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True # Found a duplicate!
            
    return False # No duplicates found

# Test case
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))

        

# Approach 2

def containsDuplicate2(nums) -> bool:
    
    duplicate=[]
    for i in nums:
        if i in duplicate:
            return True
        duplicate.append(i)

    return False # No duplicates found

# Test case
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate2(nums))