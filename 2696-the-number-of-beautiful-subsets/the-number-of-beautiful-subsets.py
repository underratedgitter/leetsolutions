class Solution:
    def beautifulSubsets(self, nums, k):
        from collections import defaultdict
        
        def backtrack(index, freq_map):
            if index == len(nums):
                return 1
            
            count = 0
            # Option 1: Exclude nums[index]
            count += backtrack(index + 1, freq_map)
            
            # Option 2: Include nums[index], only if it's beautiful
            if freq_map[nums[index] - k] == 0 and freq_map[nums[index] + k] == 0:
                freq_map[nums[index]] += 1
                count += backtrack(index + 1, freq_map)
                freq_map[nums[index]] -= 1
            
            return count
        
        freq_map = defaultdict(int)
        # Start backtracking from index 0 with an empty frequency map
        total_beautiful_subsets = backtrack(0, freq_map) - 1  # Subtract 1 to exclude the empty subset
        return total_beautiful_subsets

# Example usage:
sol = Solution()
print(sol.beautifulSubsets([2, 4, 6], 2))  # Output: 4
print(sol.beautifulSubsets([1], 1))       # Output: 1
