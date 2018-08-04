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
