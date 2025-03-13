class Solution:
    def printGfg(self, n):
        if n == 0: # Base condition
            return
        self.printGfg(n-1) # Function calling itself
        print('GFG', end=" ") # Print GFG n times