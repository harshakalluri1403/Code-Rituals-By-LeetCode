from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new=deque(nums)
        new.rotate(k)
        nums_list=list(new)
        nums[:] = nums_list
        return nums