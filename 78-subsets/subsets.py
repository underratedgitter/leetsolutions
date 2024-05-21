class Solution:
    def subsets(self, nums):
        def backtrack(start, path):
            result.append(path[:])  # Add a copy of the current path to the result

            for i in range(start, len(nums)):
                path.append(nums[i])  # Add the current number to the path
                backtrack(i + 1, path)  # Continue exploring with the next number
                path.pop()  # Backtrack by removing the last added number

        result = []
        backtrack(0, [])  # Start the backtracking process with an empty path
        return result

# Example usage
nums = [1, 2, 3]
solution = Solution()
print(solution.subsets(nums))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]