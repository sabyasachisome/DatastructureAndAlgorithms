"""
1. Two Sum
Easy 40.6K 1.3K Companies Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. Example 2:

Input: nums = [3,2,4], target = 6 Output: [1,2] Example 3:

Input: nums = [3,3], target = 6 Output: [0,1]

Constraints:

2 <= nums.length <= 104 -109 <= nums[i] <= 109 -109 <= target <= 109 Only one valid answer exists.
#
"""
from typing import List
class Solution:
    def twoSum(self,nums: List[int], target: int)-> List[int]:
        num_dict={}
        for idx in range(len(nums)):
            if target- nums[idx] in num_dict:
                return [num_dict[target- nums[idx]],idx]
            num_dict[nums[idx]]= idx

sol= Solution()
sol.twoSum([2,7,11,15],9)

"""
26. Remove Duplicates from Sorted Array
Easy 9.3K 12.9K Companies Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length; for (int i = 0; i < k; i++) { assert nums[i] == expectedNums[i]; } If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [1,1,2] Output: 2, nums = [1,2,_] Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores). Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4] Output: 5, nums = [0,1,2,3,4,,,,,_] Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

1 <= nums.length <= 3 * 104 -100 <= nums[i] <= 100 nums is sorted in non-decreasing order.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        elem_map_freq= {}
        counter=0
        for idx in range(len(nums)-1):
            if nums[idx]!=nums[idx+1]:
                counter+=1
                nums[counter]=nums[idx+1]
        return counter+1

sol= Solution()
sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])