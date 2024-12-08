class Solution(object):
    def searchRange(self, nums, target):
        result=[-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                if result[0]==-1:
                    result[0]=i
                result[1]=i
        return result