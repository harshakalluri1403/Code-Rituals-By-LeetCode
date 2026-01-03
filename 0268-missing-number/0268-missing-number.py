class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        exp=n*(n+1)//2
        add=sum(nums)
        return exp-add