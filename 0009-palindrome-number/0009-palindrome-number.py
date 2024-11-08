class Solution(object):
    def isPalindrome(self, x):
        # Convert the integer to a string and check if it's equal to its reverse
        return str(x) == str(x)[::-1]
