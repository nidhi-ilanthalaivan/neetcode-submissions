class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # so u cant go left anymre u can only go rightmost
        # keep that in mind
        # ideally u want to buy when its the cheapest price ok
        # and profit is going to be wtv the current day's profit is - cheapest price
        # no need to define left as u dont need to keep track of it
        cheapest_price = float('inf')
        profit = 0
        for right in range(len(prices)):
            cheapest_price = min(prices[right], cheapest_price)
            profit = max(profit, prices[right] - cheapest_price)
        
        return profit