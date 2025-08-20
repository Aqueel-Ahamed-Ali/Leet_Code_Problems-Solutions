class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x != 0 and x % 10 == 0:
            return False
        
        reverse = 0
        while reverse < x:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        
        return reverse == x or x == reverse // 10
