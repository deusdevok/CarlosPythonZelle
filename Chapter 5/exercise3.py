def main():
    scores = 'F'*60+'D'*10+'C'*10+'B'*10+'A'*11
    quizScore = int(input('Enter your exam score (0 to 100): '))
    grade = scores[quizScore]
    print('The grade is ', grade)
main()
