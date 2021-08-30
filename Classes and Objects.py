class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Worker(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.workyear = year

    def welcome(self):
            print("Welcome ", self.firstname, self.lastname, "to the class of ", self.workyear)

worker = Worker("Annabeth", "Chase", "2021")
worker.welcome()
