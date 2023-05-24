class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create dictionaries to map characters from s to t and vice versa
        s_to_t = {}
        t_to_s = {}
        
        # Iterate through each character in s and t simultaneously
        for char_s, char_t in zip(s, t):
            # If the character from s hasn't been seen before, map it to the corresponding character from t
            if char_s not in s_to_t:
                s_to_t[char_s] = char_t
            # If the character from s has been seen before but doesn't map to the corresponding character from t, return False
            elif s_to_t[char_s] != char_t:
                return False
            
            # Same as above but for t to s mapping
            if char_t not in t_to_s:
                t_to_s[char_t] = char_s
            elif t_to_s[char_t] != char_s:
                return False
            
        # If we've made it this far, the strings are isomorphic
        return True
