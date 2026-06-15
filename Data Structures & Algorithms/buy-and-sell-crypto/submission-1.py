class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_seen = prices[0]
        for price in prices:
            if (price - min_seen) > profit:
                profit = price - min_seen
            min_seen = min(min_seen, price)



        return profit
        