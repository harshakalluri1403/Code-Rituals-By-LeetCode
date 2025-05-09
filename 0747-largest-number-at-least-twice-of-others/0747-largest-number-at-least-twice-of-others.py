class Solution(object):
    def dominantIndex(self, nums):
        maximum=max(nums)
        maximum_index=nums.index(maximum)
        for i in range(len(nums)):
            if i!=maximum_index and maximum<2*nums[i]:
                return -1
        return maximum_index