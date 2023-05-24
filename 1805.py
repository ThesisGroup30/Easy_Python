import re

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # Replace all non-digit characters with spaces
        word = re.sub('[^0-9]', ' ', word)
        
        # Split the string into a list of integers
        integers = list(map(int, word.split()))
        
        # Return the number of unique integers
        return len(set(integers))
