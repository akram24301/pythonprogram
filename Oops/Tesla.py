class Employee:
    company='TESLA'
    CEO='Elon Musk'

    
    def insert_member(self,name,age,sal,eid):
        self.name=name
        self.age=age
        self.sal=sal
        self.eid=eid

Bhanu=Employee()
Akram=Employee()
Dhoni=Employee()

Employee.insert_member(Bhanu,'Bhanu',22,50000,201)
Employee.insert_member(Akram,'Akram',23,30000,300) 
Dhoni.insert_member('Akram',23,30000,300) 
