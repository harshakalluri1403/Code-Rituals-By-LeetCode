class Solution(object):
    def findErrorNums(self, nums):
        seen = set()
        n=len(nums)+1
        expected=sum(range(n))
        actual=sum(set(nums))
        for num in nums:
            if num in seen:
                return num, expected-actual
            seen.add(num)