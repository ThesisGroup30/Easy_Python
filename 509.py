class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            # Calculate Fibonacci numbers iteratively
            prev_prev = 0
            prev = 1
            curr = 1
            for i in range(2, n+1):
                curr = prev_prev + prev
                prev_prev = prev
                prev = curr
            return curr
