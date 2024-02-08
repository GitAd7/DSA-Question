# Intersection of Two Arrays

def intersection(a,b):
    s = {}
    for i in range(len(a)):
        if a[i] not in s:
            s[a[i]] = i
    res = 0
    for j in range(len(b)):
        if b[j] not in s:
            res += 1
        else:
            del s[b[j]]
            
    return res 

a = [10,15, 20, 15, 30,30,5]
b = [30,5,30,80]
print(f'Intersection of two arrays is:{intersection(a,b)}')

c = [10,10,10]
d = [10,10,10]
print(f'Number of Intersection points in these arrays is:{intersection(c,d)}')