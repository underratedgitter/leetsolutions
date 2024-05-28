class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        
        max_length = 0
        current_cost = 0
        start = 0
        
        for end in range(n):
            current_cost += costs[end]
            
            # If the current cost exceeds maxCost, move the start pointer to the right
            while current_cost > maxCost:
                current_cost -= costs[start]
                start += 1
            
            # Update the maximum length of the valid window
            max_length = max(max_length, end - start + 1)
        
        return max_length

# Example usage:
solution = Solution()
s1 = "abcd"
t1 = "bcdf"
maxCost1 = 3
print(solution.equalSubstring(s1, t1, maxCost1))  # Output: 3

s2 = "abcd"
t2 = "cdef"
maxCost2 = 3
print(solution.equalSubstring(s2, t2, maxCost2))  # Output: 1

s3 = "abcd"
t3 = "acde"
maxCost3 = 0
print(solution.equalSubstring(s3, t3, maxCost3))  # Output: 1
