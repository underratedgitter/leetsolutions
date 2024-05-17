class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the shortest string in the array
        shortest_str = min(strs, key=len)

        for i, char in enumerate(shortest_str):
            # Check if all strings have the character at the current position
            for s in strs:
                if s[i] != char:
                    return shortest_str[:i]

        # If all strings are the same, return the shortest string
        return shortest_str
        