class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        max_profit = 0
        for right in range(len(prices)):
            curr_min = min(curr_min, prices[right])
            max_profit = max(max_profit, prices[right] - curr_min)
        
        return max_profit