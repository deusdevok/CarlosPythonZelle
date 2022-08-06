import ast
from student import Student

# Student(name, hours(credits), qpoints)
aStudent = Student("Carlos", 0, 0)

while(True):
    
    inputFromUser = input('Enter grade points and credit hours (separated by a space): ')

    if inputFromUser.lower() == 'q':
        print('Thank you.')
        break

    gradePoint, credits = inputFromUser.split(' ')
    aStudent.addGrade(float(gradePoint), float(credits))


print('Student {} has a gpa of {}'.format(aStudent.getName(), aStudent.gpa()))