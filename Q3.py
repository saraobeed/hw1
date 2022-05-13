import json

with open('Q&A.json') as f:
    Q_and_A = json.load(f)

student = input('Enter Your name:')
mark = 0

for qa in Q_and_A:
    q , a = qa.split('=')
    student_a = input(q+'=')
    if student_a == a:
        mark = mark + 1

print('your mark is:' + str(mark))

with open('students.json') as f:
    students = json.load(f)

students[student]=mark

with open('students.json', 'w') as f:
    json.dump(students, f)
