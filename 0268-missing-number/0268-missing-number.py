class Solution(object):
    def missingNumber(self, nums):
        length=len(nums)
        expected=length*(length+1)//2
        actual=sum(nums)
        return expected-actual    