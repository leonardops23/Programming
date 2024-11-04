
class EmployeeManagement:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}\nPosition: {self.position}\nSalary: ${self.salary}"
