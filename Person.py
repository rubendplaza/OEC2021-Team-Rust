class Person:
    def __init__(self, number =0.0, lastName='', firstName='', grade=0.0, periodOne='', periodTwo='', periodThree='', periodFour='', conditions='', activities=''):
        self.number = number
        self.lastName = lastName
        self.firstName = firstName
        self.grade = grade
        self.periodOne = periodOne
        self.periodTwo = periodTwo
        self.periodThree = periodThree
        self.periodFour = periodFour
        self.conditions = conditions
        self.activities = activities
        self.infected = False
        self.howManyInfected = 0
        self.infectedBy = []
        self.infectedInPeriodNumber = 0
        self.probability = 0.0
        self.multiplier = 1
        if (int(grade) == 10):
            self.multiplier += 0.25
        elif (int(grade) == 11):
            self.multiplier += 0.50
        elif (int(grade) == 12):
            self.multiplier += 0.75

        if (conditions != "N/A"):
            self.multiplier += 0.70


    def __str__(self):
        return str(self.number) +" " +self.lastName + " " + self.firstName + " " 