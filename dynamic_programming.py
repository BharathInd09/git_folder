# Dynamic Programming


def fact(val):
    if val == 1:
        return val
    else:
        return val * fact(val - 1)


m = int(input('Enter the limit: '))
l = [0] * 100
l2 = []
c = 0
while c < m:
    n = int(input('Enter a value: '))
    if n in l2:
        print(l[n])
    else:
        result = fact(n)
        l[n] = result
        print(result)
    if n not in l2:
        l2.append(n)
    c += 1
