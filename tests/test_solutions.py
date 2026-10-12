"""Regression tests for the solution modules under repo root.

Each problem lives in its own hyphen/digit-prefixed directory, so modules
can't be imported normally -- they're loaded by file path instead.
"""
import glob
import importlib.util
import os
from typing import List, Optional

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Names LeetCode's judge provides without an import. Solutions are kept as
# submitted, so the loader supplies them; a file's own ListNode wins.
LEETCODE_GLOBALS = {"List": List, "Optional": Optional, "ListNode": ListNode, "TreeNode": TreeNode}


def load_module(relative_path):
    full_path = os.path.join(REPO_ROOT, relative_path)
    spec = importlib.util.spec_from_file_location("solution_module", full_path)
    module = importlib.util.module_from_spec(spec)
    module.__dict__.update(LEETCODE_GLOBALS)
    spec.loader.exec_module(module)
    return module


def load_solution(relative_path):
    return load_module(relative_path).Solution()


def to_linked(node_cls, values):
    head = None
    for value in reversed(values):
        head = node_cls(value, head)
    return head


def from_linked(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def to_tree(values):
    """Build a tree from LeetCode's level-order list, None marking a gap."""
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    children = iter(nodes[1:])
    for node in nodes:
        if node is None:
            continue
        node.left = next(children, None)
        node.right = next(children, None)
    return nodes[0]


SOLUTION_FILES = sorted(
    os.path.relpath(path, REPO_ROOT)
    for path in glob.glob(os.path.join(REPO_ROOT, "[0-9]*-*", "*.py"))
)


@pytest.mark.parametrize("relative_path", SOLUTION_FILES)
def test_every_solution_loads(relative_path):
    assert hasattr(load_module(relative_path), "Solution")


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


def test_distribute_coins():
    sol = load_solution("1021-distribute-coins-in-binary-tree/distribute-coins-in-binary-tree.py")
    assert sol.distributeCoins(to_tree([3, 0, 0])) == 2
    assert sol.distributeCoins(to_tree([0, 3, 0])) == 3


def test_common_chars():
    sol = load_solution("1044-find-common-characters/find-common-characters.py")
    assert sorted(sol.commonChars(["bella", "label", "roller"])) == ["e", "l", "l"]
    assert sorted(sol.commonChars(["cool", "lock", "cook"])) == ["c", "o"]


def test_height_checker():
    sol = load_solution("1137-height-checker/height-checker.py")
    assert sol.heightChecker([1, 1, 4, 2, 1, 3]) == 3
    assert sol.heightChecker([5, 1, 2, 3, 4]) == 5
    assert sol.heightChecker([1, 2, 3, 4, 5]) == 0


def test_relative_sort_array():
    sol = load_solution("1217-relative-sort-array/relative-sort-array.py")
    assert sol.relativeSortArray(
        [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]
    ) == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    assert sol.relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]) == [22, 28, 8, 6, 17, 44]


def test_roman_to_int():
    sol = load_solution("13-roman-to-integer/roman-to-integer.py")
    assert sol.romanToInt("III") == 3
    assert sol.romanToInt("LVIII") == 58
    assert sol.romanToInt("MCMXCIV") == 1994


def test_palindrome_partitioning():
    sol = load_solution("131-palindrome-partitioning/palindrome-partitioning.py")
    assert sorted(sol.partition("aab")) == [["a", "a", "b"], ["aa", "b"]]
    assert sol.partition("a") == [["a"]]


def test_equal_substring():
    sol = load_solution(
        "1321-get-equal-substrings-within-budget/get-equal-substrings-within-budget.py"
    )
    assert sol.equalSubstring("abcd", "bcdf", 3) == 3
    assert sol.equalSubstring("abcd", "cdef", 3) == 1
    assert sol.equalSubstring("abcd", "acde", 0) == 1


def test_longest_common_prefix():
    sol = load_solution("14-longest-common-prefix/longest-common-prefix.py")
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""


def test_word_break_ii():
    sol = load_solution("140-word-break-ii/word-break-ii.py")
    assert sorted(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) == [
        "cat sand dog",
        "cats and dog",
    ]
    assert sorted(
        sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
    ) == ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"]
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []


def test_letter_combinations():
    sol = load_solution(
        "17-letter-combinations-of-a-phone-number/letter-combinations-of-a-phone-number.py"
    )
    assert sorted(sol.letterCombinations("23")) == [
        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf",
    ]
    assert sol.letterCombinations("") == []
    assert sorted(sol.letterCombinations("2")) == ["a", "b", "c"]


def test_add_two_numbers():
    module = load_module("2-add-two-numbers/add-two-numbers.py")
    sol, node = module.Solution(), module.ListNode
    assert from_linked(sol.addTwoNumbers(to_linked(node, [2, 4, 3]), to_linked(node, [5, 6, 4]))) == [7, 0, 8]
    assert from_linked(sol.addTwoNumbers(to_linked(node, [0]), to_linked(node, [0]))) == [0]
    assert from_linked(
        sol.addTwoNumbers(to_linked(node, [9] * 7), to_linked(node, [9] * 4))
    ) == [8, 9, 9, 9, 0, 0, 0, 1]


def test_merge_k_lists():
    module = load_module("23-merge-k-sorted-lists/merge-k-sorted-lists.py")
    sol, node = module.Solution(), module.ListNode
    lists = [to_linked(node, v) for v in ([1, 4, 5], [1, 3, 4], [2, 6])]
    assert from_linked(sol.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert from_linked(sol.mergeKLists([])) == []
    assert from_linked(sol.mergeKLists([None])) == []


def test_reverse_k_group():
    module = load_module("25-reverse-nodes-in-k-group/reverse-nodes-in-k-group.py")
    sol, node = module.Solution(), module.ListNode
    assert from_linked(sol.reverseKGroup(to_linked(node, [1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert from_linked(sol.reverseKGroup(to_linked(node, [1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]


def test_append_characters():
    sol = load_solution(
        "2572-append-characters-to-string-to-make-subsequence/"
        "append-characters-to-string-to-make-subsequence.py"
    )
    assert sol.appendCharacters("coaching", "coding") == 4
    assert sol.appendCharacters("abcde", "a") == 0
    assert sol.appendCharacters("z", "abcde") == 5


def test_find_substring():
    sol = load_solution(
        "30-substring-with-concatenation-of-all-words/"
        "substring-with-concatenation-of-all-words.py"
    )
    assert sorted(sol.findSubstring("barfoothefoobarman", ["foo", "bar"])) == [0, 9]
    assert sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]) == []
    assert sorted(sol.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"])) == [6, 9, 12]


def test_longest_valid_parentheses():
    sol = load_solution("32-longest-valid-parentheses/longest-valid-parentheses.py")
    assert sol.longestValidParentheses("(()") == 2
    assert sol.longestValidParentheses(")()())") == 4
    assert sol.longestValidParentheses("") == 0


def test_reverse_string_in_place():
    sol = load_solution("344-reverse-string/reverse-string.py")
    s = list("hello")
    assert sol.reverseString(s) is None
    assert s == list("olleh")
    s = list("Hannah")
    sol.reverseString(s)
    assert s == list("hannaH")


def test_longest_palindrome_length():
    sol = load_solution("409-longest-palindrome/longest-palindrome.py")
    assert sol.longestPalindrome("abccccdd") == 7
    assert sol.longestPalindrome("a") == 1


def test_get_permutation():
    sol = load_solution("60-permutation-sequence/permutation-sequence.py")
    assert sol.getPermutation(3, 3) == "213"
    assert sol.getPermutation(4, 9) == "2314"
    assert sol.getPermutation(3, 1) == "123"


def test_replace_words():
    sol = load_solution("648-replace-words/replace-words.py")
    assert (
        sol.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
        == "the cat was rat by the bat"
    )
    assert sol.replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs") == "a a b c"


def test_is_number():
    sol = load_solution("65-valid-number/valid-number.py")
    for valid in ["0", "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]:
        assert sol.isNumber(valid) is True, valid
    for invalid in ["e", ".", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]:
        assert sol.isNumber(invalid) is False, invalid


def test_climb_stairs():
    sol = load_solution("70-climbing-stairs/climbing-stairs.py")
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(10) == 89


def test_is_n_straight_hand():
    sol = load_solution("876-hand-of-straights/hand-of-straights.py")
    assert sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
    assert sol.isNStraightHand([1, 2, 3, 4, 5], 4) is False
