n = int(input("Enter a number: "))
def count_digits(n):
    cnt = 0
    real_n = n
    while n > 0:
        dig = n % 10
        if dig != 0 and real_n % dig == 0:
            cnt += 1
        n = n // 10
    return cnt

print(f'The number of digits that divide {n} are: {count_digits(n)}')