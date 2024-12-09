class Solution(object):
    def addDigits(self, num):
        ans1 = sum(int(digit) for digit in str(num))
        ans2 = sum(int(digit) for digit in str(ans1))
        return ans2