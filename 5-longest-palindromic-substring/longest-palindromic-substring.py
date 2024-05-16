class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        longest = ""

        # Base case: single character is a palindrome
        for i in range(n):
            dp[i][i] = True
            longest = s[i]

        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest = s[i:i + 2]

        # Check for longer substrings
        for length in range(3, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True
                    longest = s[start:end + 1]

        return longest