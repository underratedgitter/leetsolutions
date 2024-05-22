from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start, path, res):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(s, start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path, res)
                    path.pop()

        res = []
        backtrack(0, [], res)
        return res