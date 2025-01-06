n = int(input("Enter a number: "))
def is_palindrome(n):
    if n < 0:
        return False
    org = n
    rev = 0
    while n > 0:
        dig = n % 10
        n = n // 10
        rev = rev*10 + dig
    return org == rev

print(is_palindrome(n))
# TC: O(log(n))