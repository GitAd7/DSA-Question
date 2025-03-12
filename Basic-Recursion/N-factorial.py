def fact(n): # Making a function to calculate factorial
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
class Solution:
    def factorialNumbers(self, n):
        fact_list = [] # List to store the factorial numbers
        # Loop to calculate factorial numbers
        for i in range(1, n+1):
            v = fact(i)
            if v <= n: # If the factorial number is less than or equal to n, then append it to the list
                fact_list.append(v)
            else:
                break
        return fact_list # Return the list