# Haloy Analytics


class Employee:
    employeelist=list()
    def __init__(self, empNo, empName, empDes, empSal):
        self.empNo, self.empName, self.empDes, self.empSal= empNo, empName, empDes, empSal
    def addNewEmployee(self):
        Employee.employeelist.append(self)
    def getEmplist(self):
        return Employee.employeelist
    def getEmpbyid(self,empNo):
        for emp in Employee.employeelist:
            if (emp.getEmpNo()==empNo) :
                return emp
        return False
    def updateEmployee(self,empNo,empName,empDes,empSal):
        for emp in Employee.employeelist:
            if (emp.getEmpNo()==empNo):
                emp.empNo,emp.empName,emp.empDes,emp.empSal= empNo, empName, empDes, empSal
                return True
        return False
    def removeEmployee(self,EmpNo):
        for emp in Employee.employeelist:
            if(emp.getEmpNo()==empNo):
                Employee.employeelist.remove(emp)
                return True
        return False
    def setEmpNo(self, empNo):
        self.empNo= empNo
    def getEmpNo(self):
        return self.empNo
    def setEmpName(self, empName):
        self.empName= empName
    def getEmpName(self):
        return self.empName
    def setEmpDes(self, empDes):
        self.empDes= empDes
    def getEmpDes(self):
        return self.empDes
    def setEmpSal(self, empSal):
        self.empSal= empSal
    def getEmpSal(self):
        return self.empSal
    def __str__(self):
        return '%d %s %s %d'% (self.empNo, self.empName, self.empDes, self.empSal)
    
choice=1
employee=Employee(0,'','',0)
while choice >=1 and choice<=5:
    print('1. Add New Employee\n2. Get Employee List\n3.Get Employee by id\n4.Update Employee field\n5.Remove Employee Field')
    choice=int(input('Enter Your Choice:'))
    if (choice==1):
        empNo= int(input('Enter Employee No:'))
        empName= input('Enter Employee Name:')
        empDes= input('Enter Employee Designation:')
        empSal= float(input('Enter Employee Salary:'))
        emp=Employee(empNo, empName, empDes, empSal)
        emp.addNewEmployee()

    elif (choice==2):
        print('\n')
        for emp in employee.getEmplist():
            print(emp)
    elif (choice==3):
        print('\n')
        empNo=int(input('Enter Employee number:'))
        emp= employee.getEmpbyid(empNo)
        if(emp==False):
            print('\n Sorry....! Employee Not found or id:',empNo)
        else:
            print(emp)
    elif (choice==4):
        empNo= int(input('Enter Employee No:'))
        empName= input('Enter Employee Name:')
        empDes= input('Enter Employee Designation:')
        empSal= float(input('Enter Employee Salary:'))
        emp=employee.updateEmployee(empNo, empName, empDes, empSal)
        if (emp==False):
             print('\n Sorry....! Update failed Employee Not found or id:',empNo)
        else:
            print("successully updated")
    elif(choice==5):
        empNo=int(input('Enter Employee id:'))
        emp=employee.removeEmployee(empNo)
        if (emp==False):
            print('\n Sorry! Delete ailed, Employee Not ound or id:',empNo)
        else:
            print('Successully removed Employee or id:',empNo)

            
    
