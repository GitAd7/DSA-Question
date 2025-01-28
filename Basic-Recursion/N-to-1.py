class Solution:
    def printNos(self, n):
        if n == 0:
            return
        print(n, end=" ") # Before calling the function, print the number so that we can get reverse order
        self.printNos(n-1) # Call the function with n-1