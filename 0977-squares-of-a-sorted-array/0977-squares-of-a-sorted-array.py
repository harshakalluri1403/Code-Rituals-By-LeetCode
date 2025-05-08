class Solution(object):
    ## TIME COMPLEXITY FOR BOTH IS O(nlogn) 
    ## 2nd method is more memory efficient thant 1st one 
    #def sortedSquares(self, nums):
    #    return sorted(list(map(lambda i: i ** 2, nums)))
    def sortedSquares(self, nums):
        return sorted(x ** 2 for x in nums)