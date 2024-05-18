import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Define the regular expression pattern for a valid number
        number_pattern = re.compile(
            r'^[+-]?('                  # Optional sign
            r'(\d+(\.\d*)?)|'           # Digits followed by optional dot and digits
            r'(\.\d+)'                  # Dot followed by digits
            r')([eE][+-]?\d+)?$'        # Optional exponent part
        )
        
        # Match the input string against the pattern
        return bool(number_pattern.match(s))

# Example usage:
solution = Solution()
print(solution.isNumber("0"))        # True
print(solution.isNumber("e"))        # False
print(solution.isNumber("."))        # False
print(solution.isNumber("2e10"))     # True
print(solution.isNumber("3.14"))     # True
print(solution.isNumber("-123.456e789")) # True
print(solution.isNumber("95a54e53")) # False
