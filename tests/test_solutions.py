"""Regression tests for the solution modules under repo root.

Each problem lives in its own hyphen/digit-prefixed directory, so modules
can't be imported normally -- they're loaded by file path instead.
"""
import importlib.util
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_solution(relative_path):
    full_path = os.path.join(REPO_ROOT, relative_path)
    spec = importlib.util.spec_from_file_location("solution_module", full_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()


def test_two_sum():
    sol = load_solution("1-two-sum/two-sum.py")
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]


def test_is_match():
    sol = load_solution("10-regular-expression-matching/regular-expression-matching.py")
    assert sol.isMatch("aa", "a") is False
    assert sol.isMatch("aa", "a*") is True
    assert sol.isMatch("ab", ".*") is True


def test_three_sum():
    sol = load_solution("15-3sum/3sum.py")
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol.threeSum([0, 1, 1]) == []
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]


def test_three_sum_closest():
    sol = load_solution("16-3sum-closest/3sum-closest.py")
    assert sol.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert sol.threeSumClosest([0, 0, 0], 1) == 0


def test_single_number_iii():
    sol = load_solution("260-single-number-iii/single-number-iii.py")
    assert sorted(sol.singleNumber([1, 2, 1, 3, 2, 5])) == [3, 5]
    assert sorted(sol.singleNumber([-1, 0])) == [-1, 0]


def test_beautiful_subsets():
    sol = load_solution("2696-the-number-of-beautiful-subsets/the-number-of-beautiful-subsets.py")
    assert sol.beautifulSubsets([2, 4, 6], 2) == 4
    assert sol.beautifulSubsets([1], 1) == 1


def test_length_of_longest_substring():
    sol = load_solution(
        "3-longest-substring-without-repeating-characters/"
        "longest-substring-without-repeating-characters.py"
    )
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0


def test_sudoku_solver():
    sol = load_solution("37-sudoku-solver/sudoku-solver.py")
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol.solveSudoku(board)
    expected_row0 = ["5", "3", "4", "6", "7", "8", "9", "1", "2"]
    assert board[0] == expected_row0
    # every row, column and 3x3 box must contain 1-9 exactly once
    digits = set("123456789")
    for row in board:
        assert set(row) == digits
    for col in range(9):
        assert {board[r][col] for r in range(9)} == digits


def test_find_median_sorted_arrays():
    sol = load_solution("4-median-of-two-sorted-arrays/median-of-two-sorted-arrays.py")
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5


def test_first_missing_positive():
    sol = load_solution("41-first-missing-positive/first-missing-positive.py")
    assert sol.firstMissingPositive([1, 2, 0]) == 3
    assert sol.firstMissingPositive([3, 4, -1, 1]) == 2
    assert sol.firstMissingPositive([7, 8, 9, 11, 12]) == 1


def test_longest_palindrome():
    sol = load_solution("5-longest-palindromic-substring/longest-palindromic-substring.py")
    assert sol.longestPalindrome("babad") in ("bab", "aba")
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("") == ""


def test_check_record():
    sol = load_solution("552-student-attendance-record-ii/student-attendance-record-ii.py")
    assert sol.checkRecord(2) == 8
    assert sol.checkRecord(1) == 3
    assert sol.checkRecord(10101) == 183236316


def test_zigzag_convert():
    sol = load_solution("6-zigzag-conversion/zigzag-conversion.py")
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert sol.convert("A", 1) == "A"


def test_reverse_integer():
    sol = load_solution("7-reverse-integer/reverse-integer.py")
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
    assert sol.reverse(120) == 21
    assert sol.reverse(1534236469) == 0  # overflows 32-bit signed range


def test_subsets():
    sol = load_solution("78-subsets/subsets.py")
    result = sol.subsets([1, 2, 3])
    expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert sorted(result) == sorted(expected)


def test_my_atoi():
    sol = load_solution("8-string-to-integer-atoi/string-to-integer-atoi.py")
    assert sol.myAtoi("42") == 42
    assert sol.myAtoi("   -42") == -42
    assert sol.myAtoi("4193 with words") == 4193
    assert sol.myAtoi("words and 987") == 0
    assert sol.myAtoi("-91283472332") == -(2**31)


def test_is_palindrome():
    sol = load_solution("9-palindrome-number/palindrome-number.py")
    assert sol.isPalindrome(121) is True
    assert sol.isPalindrome(-121) is False
    assert sol.isPalindrome(10) is False


def test_int_to_roman():
    sol = load_solution("12-integer-to-roman/integer-to-roman.py")
    assert sol.intToRoman(3749) == "MMMDCCXLIX"
    assert sol.intToRoman(58) == "LVIII"
    assert sol.intToRoman(1994) == "MCMXCIV"
