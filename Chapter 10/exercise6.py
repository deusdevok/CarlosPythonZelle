from student import Student

# Student(name, hours(credits), qpoints)
aStudent = Student("Carlos", 0, 0)

while(True):
    
    inputFromUser = input('Enter grade letter points (A, A-, B, C, D) and credit hours (separated by a space, Q to quit): ')

    if inputFromUser.lower() == 'q':
        print('Thank you.')
        break

    gradePoint, credits = inputFromUser.split(' ')
    aStudent.addLetterGrade(gradePoint, float(credits))


print('Student {} has a gpa of {}'.format(aStudent.getName(), aStudent.gpa()))