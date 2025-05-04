class Solution(object):
    def findDisappearedNumbers(self, nums):
        original=set(nums)
        length=len(nums)
        duplicate=set(range(1,length+1))
        return list(duplicate-original)