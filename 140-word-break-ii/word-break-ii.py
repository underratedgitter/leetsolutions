from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Convert wordDict to a set for faster lookup
        word_set = set(wordDict)
        
        # Memoization dictionary
        memo = {}
        
        def backtrack(start: int) -> List[str]:
            # If we have already computed the result for this start index, return it
            if start in memo:
                return memo[start]
            
            # If we have reached the end of the string, return a list with an empty string
            if start == len(s):
                return [""]
            
            # To store the results for the current start index
            result = []
            
            # Iterate through the string and try every possible end index
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Recursive call to get the sentences for the rest of the string
                    sub_sentences = backtrack(end)
                    for sub_sentence in sub_sentences:
                        # If sub_sentence is empty, it means we have reached the end of the string
                        if sub_sentence:
                            result.append(word + " " + sub_sentence)
                        else:
                            result.append(word)
            
            # Store the result in memo dictionary
            memo[start] = result
            return result
        
        # Start the backtracking from index 0
        return backtrack(0)

    def beautifulSubsets(self, param_1, param_2):
        # Placeholder implementation for the beautifulSubsets method
        # Replace this with the actual implementation when available
        pass

# Example Usage for wordBreak
s1 = "catsanddog"
wordDict1 = ["cat", "cats", "and", "sand", "dog"]
solution = Solution()
print(solution.wordBreak(s1, wordDict1))  # Output: ["cats and dog", "cat sand dog"]

s2 = "pineapplepenapple"
wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
print(solution.wordBreak(s2, wordDict2))  # Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(solution.wordBreak(s3, wordDict3))  # Output: []
