class Employee: #creating a class Employee
    def __init__(self,name,ID_number, department, job_title):
        #initializing name, ID number, department, job title
        self._name = name
        self._ID = ID_number
        self._department = department
        self._job = job_title
    def printEmployee(self): #printing name, ID number, department, job title
        print("Name:",self._name)
        print("ID number:",self._ID)
        print("Department:",self._department)
        print("Title:",self._job)
        print() 

def main(): #defining main
    emp1=Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    emp2=Employee('Mark Jones', 39119, 'IT','Programmer')
    emp3=Employee('Joy Rogers',81774,'Manufacturing','Engineer')
    #storing datas of Employee in emp1,emp2 and emp3
    print("Employee 1:")
    emp1.printEmployee()
    print("Employee 2:")
    emp2.printEmployee()
    print("Employee 3:")
    emp3.printEmployee()
    #prints employee 1,2 and 3
main()
