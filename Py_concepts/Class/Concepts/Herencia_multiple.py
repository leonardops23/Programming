
class CompanyMembers:
    def __init__(self,
                name, 
                lastname,
                area,
                postion, 
                salary, 
                available) -> None:

        self.name = name
        self.lastname = lastname
        self.area = area
        self.position = postion
        self.salary = salary
        self.available = available

    def show_info(self) -> str:
        return f"""
                Info Company Members

                Name = {self.name}
                Lastname = {self.lastname}
                Area = {self.area}
                Position = {self.position}
                Salary = {self.salary}
                Available = {self.available}
                """

class AssitentManage(CompanyMembers):
    def __init__(self,name, lastname, area, postion, salary,
                available, food, bono, completed_tasks) -> None:
        super().__init__(name, lastname, area, postion, salary, available)
        self.bono = bono
        self.food = food
        self.completed_tasks = completed_tasks

    def is_bono(self):
        if self.completed_tasks == True:
            self.salary += 120
        else:
            print("You haven't bono")


def menu():
    is_members = "\nChoose according to your position: "
    name = input("Enter your name: ")
    lastname = input("Enter your lastname: ")
    area = ""
    area_option = [
        "Tech",
        "Human Resources",
        "Company Parsters",
        "Psychology",
        "Administrator",
    ]

    position_tech = [
        "Developer Junior",
        "Developer Senior",
        "Developer web",
        "Enginners",
    ]

    print(is_members)
    for index, area in enumerate(area_option):
        print(f"{index + 1}.- {area}")

    area = input(f"Select one of the options [1 - {len(area_option)}]: ")

    if area == "1":
        print("tech")
    elif area == "2":
        print("Human Resoutser")
    elif area == "3":
        print("Company")
    elif area == "4":
        print("Psy")
    elif area == "5":
        print("AD")
    else:
        print("Select one of range, try again")

    position = input("Position: ")
    salary = input("Salary: ")
    available = input("Is available: ")

    while True:
        position

        

def main():
    options_imput = menu()

empleado = CompanyMembers("Jose", "Alberto", "Tech", "Programador", 1300, True)


if __name__ == "__main__":
    main()