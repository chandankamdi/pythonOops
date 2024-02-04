#relation: part of: both are interdependent. strong connection. strong association

class Salary:
    def __init__(self,pay,reward):
        self.pay=pay
        self.reward=reward
    
    def annual_salary(self):
        return (self.pay*12)+self.reward
    
class Employee:
    def __init__(self,name,position,pay,reward):
        self.name=name
        self.position=position
        self.final_salary=Salary(pay,reward)       #here attribute self.fial_salary became a object as class Salary was called within it
        
    def employee_salary(self):
        return self.final_salary.annual_salary()    #so here while calling function within Salary, we used attribute self.final_salary

emp=Employee("Chandan","Manager",25000,2000)
print(emp.employee_salary())
