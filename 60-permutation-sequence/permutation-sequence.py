from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of digits to choose from
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # Adjust k to be 0-based
        result = []
        fact = factorial(n - 1)

        # Compute the permutation
        for i in range(n):
            idx = k // fact
            result.append(nums.pop(idx))
            k %= fact
            if i < n - 1:
                fact //= (n - i - 1)

        return ''.join(result)