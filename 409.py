class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        odd_count = 0
        has_odd = False
        for count in char_count.values():
            if count % 2 == 1:
                odd_count += 1
                has_odd = True
        if has_odd:
            return len(s) - odd_count + 1
        else:
            return len(s)
