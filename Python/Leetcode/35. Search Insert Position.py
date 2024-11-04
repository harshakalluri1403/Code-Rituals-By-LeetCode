class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)
        