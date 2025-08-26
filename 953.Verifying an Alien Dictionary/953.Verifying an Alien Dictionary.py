from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a mapping of alien order to character indices
        char_map = {c: i for i, c in enumerate(order)}
        
        # Compare each pair of adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            # Compare characters of both words
            for j in range(len(word1)):
                # If word2 is exhausted before word1, it should come after (prefix rule)
                if j >= len(word2):
                    return False
                
                # If characters differ, check if they're in correct order
                if word1[j] != word2[j]:
                    if char_map[word1[j]] > char_map[word2[j]]:
                        return False
                    break  # No need to check further characters
                
        return True
