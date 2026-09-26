from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its correct position nums[i] - 1
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # After rearranging, find the first index where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all indices are correct, the smallest missing positive is n + 1
        return n + 1
