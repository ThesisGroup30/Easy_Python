class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        if length >= 104 or width >= 104 or height >= 104 or volume >= 10**9:
            if mass >= 100:
                return "Both"
            else:
                return "Bulky"
        elif mass >= 100:
            return "Heavy"
        else:
            return "Neither"
