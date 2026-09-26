from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, path: List[int]) -> None:
            result.append(path[:])  # Add a copy of the current path to the result

            for i in range(start, len(nums)):
                path.append(nums[i])  # Add the current number to the path
                backtrack(i + 1, path)  # Continue exploring with the next number
                path.pop()  # Backtrack by removing the last added number

        result = []
        backtrack(0, [])  # Start the backtracking process with an empty path
        return result