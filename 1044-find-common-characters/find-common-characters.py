from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the frequency counter with the first word
        freq_counter = Counter(words[0])
        
        # Intersect the frequency counters of all words
        for word in words[1:]:
            freq_counter &= Counter(word)
        
        # Build the output list from the remaining characters
        output = []
        for char, count in freq_counter.items():
            output.extend([char] * count)
        
        return output