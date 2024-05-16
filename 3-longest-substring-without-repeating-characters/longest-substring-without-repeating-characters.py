class Solution:
    def lengthOfLongestSubstring(self, s):
        # Initialize pointers and variables
        left, max_len = 0, 0
        char_index = {}

        # Iterate through the string
        for right in range(len(s)):
            # If the character at index `right` is in the hashmap
            if s[right] in char_index:
                # Move the `left` pointer to the right of the repeated character
                left = max(left, char_index[s[right]] + 1)

            # Update the index of the character in the hashmap
            char_index[s[right]] = right

            # Update the maximum length of the substring
            max_len = max(max_len, right - left + 1)

        return max_len