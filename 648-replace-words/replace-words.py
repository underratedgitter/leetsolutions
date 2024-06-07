class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Create a root set from the dictionary
        root_set = set(dictionary)
        
        def replace_word(word: str) -> str:
            # Find the shortest root that forms the word
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in root_set:
                    return prefix
            return word
        
        # Split the sentence into words
        words = sentence.split()
        
        # Replace each word with its root (if applicable)
        replaced_words = [replace_word(word) for word in words]
        
        # Join the replaced words back into a sentence
        replaced_sentence = ' '.join(replaced_words)
        
        return replaced_sentence