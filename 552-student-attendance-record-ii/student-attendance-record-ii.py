class Solution:
    def checkRecord(self, n):
        MOD = 10**9 + 7

        # dp[length][absents][late_streak]
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        # Initial conditions for sequences of length 1
        dp[1][0][0] = 1  # "P"
        dp[1][0][1] = 1  # "L"
        dp[1][1][0] = 1  # "A"

        for length in range(2, n + 1):
            for absents in range(2):
                for late_streak in range(3):
                    # If the last character is 'P'
                    dp[length][absents][0] += dp[length - 1][absents][late_streak]
                    dp[length][absents][0] %= MOD

                    # If the last character is 'L' and late_streak > 0
                    if late_streak > 0:
                        dp[length][absents][late_streak] += dp[length - 1][absents][late_streak - 1]
                        dp[length][absents][late_streak] %= MOD

                    # If the last character is 'A' and absents > 0
                    if absents > 0:
                        dp[length][absents][0] += dp[length - 1][absents - 1][late_streak]
                        dp[length][absents][0] %= MOD

        # Sum up all valid sequences of length n
        result = 0
        for absents in range(2):
            for late_streak in range(3):
                result += dp[n][absents][late_streak]
                result %= MOD

        return result

# Example usage:
solution = Solution()
print(solution.checkRecord(2))   # Output: 8
print(solution.checkRecord(1))   # Output: 3
print(solution.checkRecord(10101))  # Output: 183236316
