class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # If the current sum is exactly equal to the target
        
        return closest_sum

# Example usage:
solution = Solution()
print(solution.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
print(solution.threeSumClosest([0, 0, 0], 1))       # Output: 0

