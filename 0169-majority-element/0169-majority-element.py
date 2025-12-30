class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=(len(nums))/2
        distinct_set=set(nums)
        distinct=list(distinct_set)
        maj=-math.inf
        for i in range(len(distinct)):
            count=nums.count(distinct[i])
            maj=max(maj,count)
            if majority<maj:
                return distinct[i]