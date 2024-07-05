# # 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=1
        if len(nums)==1:
            return nums
        for i in nums:
            if nums[l]==0 and nums[r]!=0:
                nums[l]=nums[r]
                nums[r]=0
                l+=1
                r+=1
            elif nums[l]!=0 and nums[r]==0:
                l+=1
                r+=1                
            elif nums[l]!=0 and nums[r]!=0:
                l+=1
                r+=1                
            else:
                r+=1
            if r==len(nums):
                break
        return nums

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
        return nums

