class Solution:
    def intToRoman(self, num):
        # Define the symbols and their corresponding values
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_numeral = ''
        
        # Iterate through the values and append the corresponding symbols
        for i in range(len(values)):
            while num >= values[i]:
                roman_numeral += symbols[i]
                num -= values[i]
        
        return roman_numeral

# Test cases
solution = Solution()
print(solution.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(solution.intToRoman(58))    # Output: "LVIII"
print(solution.intToRoman(1994))  # Output: "MCMXCIV"
