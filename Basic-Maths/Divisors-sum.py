# To print all the divisors
# n = int(input('Enter a number: '))
# def Divisors(n):
#     divisors = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             divisors.append(i)
#     return divisors

# Now for the sum of all divisors 
def SumOfDivisors(n):
    sum = 0
    for i in range(1, n+1):
        sum += i * (n//i)
    return sum