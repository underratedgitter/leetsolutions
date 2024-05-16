class Solution:
    def isPalindrome(self, x):
        # Handle negative numbers and single-digit numbers
        if x < 0 or (x < 10 and x >= 0):
            return x >= 0

        # Initialize a variable to store the reversed number
        reversed_num = 0
        original_num = x

        # Reverse the second half of the number
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        # Check if the original number is equal to the reversed number
        return original_num == reversed_num
        