# student.py

"""student.py
Provides a simple class definition for a student
with different methods and variables
"""

class Student:
    """Defines a student by its name, hours and qpoints
    also computes different aspects such as its gpa
    """
    def __init__(self, name, hours, qpoints):
        """Create a student with given name, 
        hours and qpoints
        """
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        """Returns the name
        """
        return self.name

    def getHours(self):
        """Returns the hours
        """
        return self.hours

    def getQPoints(self):
        """Returns the points
        """
        return self.qpoints

    def gpa(self):
        """Computes the Grade Point Average (gpa) for
        the current student, given the qpoints and hours
        """
        return self.qpoints/self.hours

    def addGrade(self, gradePoint, credits):
        """
        gradePoint: grade, A=4.0, A-=3.7, B+=3.3, etc (float)
        credits: number of credit hours for the class (float)
        """

        # qpoints (quality points): grade points * credit hours
        self.qpoints += gradePoint*credits
        self.hours += credits

    def addLetterGrade(self, gradeLetter, credits):
        """
        gradeLetter: grade, A, B, C, etc (string)
        credits: number of credit hours for the class (float)
        """
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

