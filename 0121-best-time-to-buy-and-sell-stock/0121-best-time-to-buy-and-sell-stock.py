class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest= float('inf')
        best_profit=0
        for price in prices:
            lowest = min(lowest, price)# the lowest price we saw till now
            best_profit = max(best_profit, price-lowest)
        
        return best_profit
