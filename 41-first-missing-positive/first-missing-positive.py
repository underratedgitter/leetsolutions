class Solution:
    def firstMissingPositive(self, nums):
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

# Example usage:
solution = Solution()
print(solution.firstMissingPositive([1, 2, 0]))      # Output: 3
print(solution.firstMissingPositive([3, 4, -1, 1]))  # Output: 2
print(solution.firstMissingPositive([7, 8, 9, 11, 12]))  # Output: 1
