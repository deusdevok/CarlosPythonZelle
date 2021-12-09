def grade(score):
	scores = 'F'*60+'D'*10+'C'*10+'B'*10+'A'*11
	gradeR = scores[score]
	return gradeR

def main():
    quizScore = int(input('Enter your exam score (0 to 100): '))
    print('The grade is ', grade(quizScore))

main()