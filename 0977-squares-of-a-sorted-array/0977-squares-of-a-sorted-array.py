class Solution(object):
    def sortedSquares(self, nums):
        return sorted(list(map(lambda i: i ** 2, nums)))
