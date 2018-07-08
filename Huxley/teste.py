grade = 0.8
grade = (0.8 * grade) + (0.2 + 0.5)

print(grade)

student = {'name': 'Thiago', 'age': 20, 'courses': ['P3', 'PAA']}

student.update({'name': 'Glauber', 'phone': '(82)98860-8635'})
#age = student.pop('age')
del student['phone']

#print(student.get('phone', 'Not Found'))
#print(student)
#print(student.keys())
#print(student.values())
#print(student.items())
#print(len(student))
#print(age)

for key, value in student.items():
    print(key, value)
