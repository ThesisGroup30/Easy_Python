class Solution:
    def toLowerCase(self, s: str) -> str:
        # Create an empty string to store the result
        result = ''
        
        # Iterate through the characters of the input string
        for char in s:
            # If the character is uppercase, convert it to lowercase
            if char.isupper():
                result += char.lower()
            else:
                result += char
        
        return result
