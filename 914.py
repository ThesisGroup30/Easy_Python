from collections import Counter
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Count the frequency of each number in the deck
        count = Counter(deck)

        # Find the greatest common divisor of all frequencies
        gcd_value = count[deck[0]]
        for freq in count.values():
            gcd_value = gcd(gcd_value, freq)

        # If gcd is greater than or equal to 2, return True, otherwise False
        return gcd_value >= 2
