class Employee:
    """
    
    Employee class to represent an employee with name and salary.

    Attributes:
        name (str): The name of the employee.
        salary (float): The salary of the employee.
        employee_count (int): Class variable to keep track of the number of employees.

    Methods:
        NumberOfEmployees(cls): Class method to print the total number of employees.
        EmployeeInformation(self): Instance method to print the employee's information.
    """


    employee_count = 0

    def __init__(self, name : str, salary : float):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    @classmethod
    def NumberOfEmployees(cls):
        print(f"Total number of employees: {cls.employee_count}")

    def EmployeeInformation(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Test.
emp1 = Employee("Alice", 50000)
emp1.EmployeeInformation()
Employee.NumberOfEmployees()
emp2 = Employee("Bob", 60000)
emp2.EmployeeInformation()  
emp3 = Employee("Charlie", 70000)
emp3.EmployeeInformation()
Employee.NumberOfEmployees()

# Display class information
print(f"Base classes: {Employee.__bases__} \n")
print(f"Class namespace: {Employee.__dict__} \n")
print(f"Class name: {Employee.__name__} \n")
print(f"Module name: {Employee.__module__} \n")
print(f"Documentation: {Employee.__doc__}")