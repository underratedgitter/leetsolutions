class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        i = 0  # Index for s
        j = 0  # Index for t

        while i < m and j < n:
            if s[i] == t[j]:
                j += 1
            i += 1

        # If j reaches the end of t, it means t is already a subsequence of s
        if j == n:
            return 0

        # Otherwise, we need to append the remaining characters of t to s
        return n - j