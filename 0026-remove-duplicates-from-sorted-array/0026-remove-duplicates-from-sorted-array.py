class Solution(object):
    def removeDuplicates(self, nums):
        # Pointer for the unique element position
        k = 1

        # Traverse through the sorted array and move unique elements forward
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
