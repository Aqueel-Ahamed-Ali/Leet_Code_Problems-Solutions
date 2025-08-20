class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Initialize variables
        original = x
        reversed_num = 0
        
        # Reverse the number
        while x > 0:
            digit = x % 10  # Get last digit
            reversed_num = reversed_num * 10 + digit  # Build reversed number
            x //= 10  # Remove last digit
        
        # Compare original with reversed
        return original == reversed_num
