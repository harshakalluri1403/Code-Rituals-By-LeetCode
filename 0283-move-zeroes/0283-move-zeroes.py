class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a=0
        number=nums.count(0)
        arr=[x for x in nums if x!=0]
        arr.extend([a]*number)
        nums[:] = arr