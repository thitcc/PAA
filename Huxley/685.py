size = int(input())
food = 0
max_carry = 0
switch = True

for i in range(0, size):
    for j in input().split():
        if switch:
            for x in j:
                if x == 'o':
                    food += 1
                elif x == 'A':
                    if food > max_carry:
                        max_carry = food
                    food = 0
            switch = False
        else:
            for x in range(size-1, -1, -1):
                if j[x] == 'o':
                    food += 1
                elif j[x] == 'A':
                    if food > max_carry:
                        max_carry = food
                    food = 0
            switch = True
        if food > max_carry:
            max_carry = food

print(max_carry)
