class Solution:
    def reverse(self, x):
        # Check if the number is negative
        is_negative = x < 0
        
        # Convert the number to a positive integer
        x = abs(x)
        
        # Reverse the digits
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        # Handle the negative case
        if is_negative:
            reversed_num = -reversed_num
        
        # Check for overflow
        if reversed_num < -(2**31) or reversed_num > (2**31 - 1):
            return 0
        
        return reversed_num