class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        profit = 0

        for i in prices:
            minprice = min(minprice,i)
            profit = max(profit , i-minprice)
        return profit