class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = []

        def backtrack(combination, next_digits):
            if not next_digits:
                combinations.append(combination)
            else:
                for letter in digit_map[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        backtrack('', digits)
        return combinations