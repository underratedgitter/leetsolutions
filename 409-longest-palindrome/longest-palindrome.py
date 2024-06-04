class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count the frequency of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Initialize result with the sum of even frequencies
        result = sum(count // 2 * 2 for count in char_count.values())

        # Check if there is at least one character with an odd frequency
        # If so, we can include one of them in the middle of the palindrome
        has_odd_freq = any(count % 2 == 1 for count in char_count.values())
        if has_odd_freq:
            result += 1

        return result
        