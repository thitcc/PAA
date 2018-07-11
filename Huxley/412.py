display = int(input())
quantity = int(input())

friends = {}

for i in range(quantity):
    id, grade = input().split()
    grade = float(grade)
    friends.update({id: grade})

feed = int(input())
updates = []

for i in range(feed):
    line = input().split(' ')
    msg = ' '.join(line[2:])
    grade = (0.8 * friends.get(line[0])) + (0.2 * float(line[1]))
    updates.append([grade, line[0], msg])

updates = sorted(updates, key=lambda x: x[0], reverse=True)

for i in range(display):
    print(updates[i][1], updates[i][2])
