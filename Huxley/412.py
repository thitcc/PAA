# Fórmula :
# 0.8 * grau de proximidade + 0.2 * tempo de atualização

feed = int(input())
quantity = int(input())

friends = {}

for i in range(quantity):
    id, grade = input().split()
    id = int(id)
    grade = float(grade)
    friends.update({id: grade})

updates = int(input())

for i in range(updates):
    id, att = input().split()
    id = int(id)
    att = float(att)
    att = (0.8 * friends.get(id)) + (0.2 * att)
    friends.update({id: att})

print(friends)
