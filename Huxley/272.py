PROD = 1

while True:

    try:
        value = int(input())
        PROD *= value
    except EOFError:
        break

print("Prod =", PROD)
