class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

    def addGrade(self, gradePoint, credits):
        '''
        gradePoint: grade, A=4.0, A-=3.7, B+=3.3, etc (float)
        credits: number of credit hours for the class (float)
        '''

        # qpoints (quality points): grade points * credit hours
        self.qpoints += gradePoint*credits
        self.hours += credits

    def addLetterGrade(self, gradeLetter, credits):
        '''
        gradeLetter: grade, A, B, C, etc (string)
        credits: number of credit hours for the class (float)
        '''
        letter = gradeLetter[0].upper()
        sign = gradeLetter[1]

        points = 0.0

        if letter == 'A':
            points = 4.0
        elif letter == 'B':
            points = 3.0
        elif letter == 'C':
            points = 2.0
        elif letter == 'D':
            points = 1.0
        else:
            points = 0.0

        if sign == '+':
            points += .33
        elif sign == '-':
            points -= .33

        self.qpoints += points*credits

        self.hours += credits
