class Employee:
    def __init__(self,empid,empname,empsal,empdept):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
        self.empdept=empdept
        
    def display(self):
        print(self.empid)

class Timesheet:
    def __init__(self,date,numofhrs,activity,description,status):
        self.date=date
        self.numofhrs=numofhrs
        self.activity=activity
        self.description=description
        self.status=status

    def display(self):
        print(self.date)
e= Employee(20522,"vaishnavi",30000,"trainee")
t= Timesheet(29,8,"python","oops","inprogess")

e.display()
t.display()
'''print(e.empid)
print(t.date)
'''
