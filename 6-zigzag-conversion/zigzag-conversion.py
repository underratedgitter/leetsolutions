class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        rows = [''] * numRows
        row = 0
        step = 1

        for char in s:
            rows[row] += char
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        return ''.join(rows)