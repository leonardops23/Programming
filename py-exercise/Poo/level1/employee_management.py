
class EmployeeManagement:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_employee(self):
        return f"Name: {self.name}\nPosition: {self.position}\nSalary: ${self.salary}"

manager = EmployeeManagement("Ivan", "Gerente", 1100)

print(manager.display_employee())
