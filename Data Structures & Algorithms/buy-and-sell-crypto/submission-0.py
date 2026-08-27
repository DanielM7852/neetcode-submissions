class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for num in prices[1:]:
            current_profit = num - min_price
            max_profit = max(current_profit,max_profit)
            min_price = min(num, min_price)
        return max_profit
