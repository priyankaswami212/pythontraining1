'''CASESTUDY'''

class Employee:
    def __init__(self,empid,empname,empsal,empdept):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
        self.empdept=empdept
    def display(self):
        print('empid= ',self.empid)
        print('name= ',self.empname)
        print('salary=', self.empsal)
        print('dept= ',self.empdept)

class Timesheet(Employee):
    def __init__(self,date,noofhrs,activity,description,status,empid,empname,empsal,empdept):
        Employee.__init__(self,empid,empname,empsal,empdept)
        self.date=date
        self.noofhrs=noofhrs
        self.activity=activity
        self.description=description
        self.status=status
    def display(self):
        print('date=',self.date)
        print('noofhrs=',self.noofhrs)
        print('activity=',self.activity)
        print('description=',self.description)
        print('status=',self.status)
    def timedetails(self):
        self.date=input('date=')
        self.noofhrs=int(input('noofhrs'))
        self.activity=input('activity')
        self.description=input('description')
        self.status=input('status')
        print("details submitted")

e1=Employee(1345,'priya',25000,'do')
e1.display()
e1=Timesheet('28/09/2021',8,'python training','basics','completed',1345,'priya',25000,'do')
e1.display()
e1.timedetails()
if(e1.noofhrs<8 and e1.noofhrs>=0):

    e1.display()
else:
    print("invalid no of hours")