class Solution:
    def myAtoi(self, s):
        # Step 1: Whitespace
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Signedness
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Step 3: Conversion
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)

        # Step 4: Rounding
        result *= sign
        if result < -(2**31):
            return -(2**31)
        elif result > (2**31 - 1):
            return (2**31 - 1)

        return result