class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert to string and compare with reverse
        return str(x) == str(x)[::-1]
