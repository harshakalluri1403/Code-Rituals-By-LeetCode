class Solution(object):
    #def sortedSquares(self, nums):
    #    return sorted(list(map(lambda i: i ** 2, nums)))
    def sortedSquares(self, nums):
        return sorted(x ** 2 for x in nums)