class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Initialize counts of $5 and $10 bills to 0
        count_5, count_10 = 0, 0
        
        # Iterate through each customer's bill
        for bill in bills:
            # Handle $5 bill
            if bill == 5:
                count_5 += 1
            # Handle $10 bill
            elif bill == 10:
                # If no $5 bills are available, return False
                if count_5 == 0:
                    return False
                count_5 -= 1
                count_10 += 1
            # Handle $20 bill
            elif bill == 20:
                # If one $10 and one $5 bill are available, use them
                if count_10 > 0 and count_5 > 0:
                    count_10 -= 1
                    count_5 -= 1
                # If three $5 bills are available, use them
                elif count_5 >= 3:
                    count_5 -= 3
                # Otherwise, return False
                else:
                    return False
        
        # All customers received correct change
        return True
