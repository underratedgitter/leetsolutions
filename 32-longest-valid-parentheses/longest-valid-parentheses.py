class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize the stack with -1
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()  # Pop the top element from the stack
                if not stack:
                    stack.append(i)  # If the stack is empty, push the current index
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length