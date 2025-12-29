class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = math.inf
        profit=0
        for i in range(len(prices)):
            minimum=min(minimum,prices[i])
            profit=max(prices[i]-minimum,profit)
        return profit        
