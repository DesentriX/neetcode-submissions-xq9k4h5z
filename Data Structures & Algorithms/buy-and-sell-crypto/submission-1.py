class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        test = sorted(prices,reverse = True)

        if prices == test:
            return profit
    
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                current = prices[j] - prices[i]
                profit = max(current, profit)
        return profit
            


        