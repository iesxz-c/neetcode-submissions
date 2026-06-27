class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit =0
        for price in prices[1:]:
            if price > buy :
                profit += price-buy
            buy = price 
        return profit
        # p=0
        # for i in range(1,len(prices)):
        #     if prices[i] > prices[i-1]:
        #         p+=prices[i] - prices[i-1]
        # return p