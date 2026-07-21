class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = prices[0]
        best_profit = 0
        for right in range(len(prices)):
            lowest_buy = min(lowest_buy, prices[right])
            best_profit = max(best_profit, prices[right] - lowest_buy)
        
        return best_profit
                