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