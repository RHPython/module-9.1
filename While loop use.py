student = []

while True:
    name = input('Enter student name:')
    if name == 'Sesh':
        print(student)
        print('Total Students:',len(student))
        break
    else:
        student.append(name)