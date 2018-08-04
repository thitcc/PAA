def powering(x, n):
    if n == 0:
        return 1

    if n == 1:
        return x

    if n % 2 == 0:
        half = powering(x, n/2)
        return half * half
    else:
        half = powering(x, (n-1) / 2)
        return half * half * x


while True:
    try:
        n1, n2 = [int(x) for x in input().split()]
        r1 = powering(n1, n1) % 100
        r2 = powering(n2, n2) % 100
        if r1 > r2:
            print(n1)
        elif r2 > r1:
            print(n2)
        else:
            print(0)
    except EOFError:
        break
