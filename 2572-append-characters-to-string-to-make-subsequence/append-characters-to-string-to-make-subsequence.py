class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        s_iter = iter(s)
        for i,c in enumerate(t):
            if c not in s_iter:
                return n-i
        return 0