class Solution:
    def fib(self, n: int) -> int:
        # Handle base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # Initialize variables for F(0) and F(1)
        prev, curr = 0, 1
        
        # Iterate to compute F(n)
        for i in range(2, n + 1):
            prev, curr = curr, prev + curr
        
        return curr
