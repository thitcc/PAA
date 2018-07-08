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
    grade = friends.get(int(line[0])) # Get the grade by ID

    #friends[int(line[0])] = (0.8 * friends[int(line[0])]) + (0.2 * float(line[1]))
    #friends.update({line[0]: [grade, line[0], msg]})

#friends = sorted(friends.values(), key=lambda x: x[0], reverse=True)

#for i in range(display):
    #print(friends[i][1], friends[i][2])
