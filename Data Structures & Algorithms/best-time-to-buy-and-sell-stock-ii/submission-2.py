class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit =0
        for i in prices[1:]:
            if i > buy:
                profit += i-buy
            buy = i
        return profit

        # p=0
        # for i in range(1,len(prices)):
        #     if prices[i] > prices[i-1]:
        #         p+=prices[i] - prices[i-1]
        # return p