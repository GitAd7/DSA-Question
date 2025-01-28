class Solution:
    def sumOfSeries(self,n):
        if n == 1: # base case
            return 1
        return n*n*n + self.sumOfSeries(n-1) # recursive case