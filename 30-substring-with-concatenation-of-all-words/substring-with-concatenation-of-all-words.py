class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import defaultdict
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = len(words) * word_len
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1

        result = []
        for i in range(len(s) - total_len + 1):
            seen = defaultdict(int)
            j = 0
            while j < len(words):
                word = s[i + j * word_len:i + (j + 1) * word_len]
                if word not in word_count:
                    break
                seen[word] += 1
                if seen[word] > word_count[word]:
                    break
                j += 1
            else:
                result.append(i)

        return result
        