n = int(input('Enter a number: '))
def Armstrong(n):
    sum = 0
    org = n
    while n > 0:
        digit = n % 10
        sum += digit ** 3
        n //= 10
    return org == sum

print(Armstrong(n))
# TC: O(log(n))