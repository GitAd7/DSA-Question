def reverse(self, x: int) -> int:
        revn = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x>0:
            dig = x % 10
            x = x // 10
            revn = revn*10 + dig
            if revn < -2**31 or revn > 2**31 - 1:
                return 0
        return revn*sign
    
x = int(input("Enter a number: "))
print(f'The reverse of {x} is: {reverse(x)}')