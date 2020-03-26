class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, id, scores):
        # to print a pirnt person function in the Person class we just neep
        # called them
        Person.__init__(self, firstName, lastName, id)
        self.score = scores
    def calculate(self):
        score = self.score
        grade = sum(score)/(len(score))
        grading = ""
        if grade >= 90 and grade <= 100:
            grading = "O"
        elif grade >= 80 and grade < 90:
            grading = "E"
        elif grade >= 70 and grade < 80:
            grading ="A"
        elif grade >= 55 and grade < 70:
            grading = "P"
        elif grade >= 40 and grade < 55:
            grading = "D"
        elif grade < 40:
            grading = "T"
        return grading

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
