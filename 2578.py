class Solution:
    def splitNum(self, num: int) -> int:
        # Count the frequency of each digit in num
        freq = [0] * 10
        for d in str(num):
            freq[int(d)] += 1
        
        # Find the minimum possible sum
        sum1, sum2 = 0, 0
        for d in range(1, 10):
            # If digit d occurs in num, split it into num1 and num2
            if freq[d] > 0:
                # Add d to the number with the smaller sum so far
                if sum1 <= sum2:
                    sum1 = sum1 * 10 + d
                else:
                    sum2 = sum2 * 10 + d
                freq[d] -= 1
            # Add any remaining occurrences of d to the number with the larger sum
            while freq[d] > 0:
                if sum1 <= sum2:
                    sum2 = sum2 * 10 + d
                else:
                    sum1 = sum1 * 10 + d
                freq[d] -= 1
        
        return sum1 + sum2
