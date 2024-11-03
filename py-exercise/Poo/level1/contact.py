class Contact:
    def __init__(self, name, telephone, address) -> None:
        self.name = name
        self.telephone = telephone
        self.address = address


    def __str__(self) -> str:
        return f"{self.name} {self.telephone} {self.address}"    

person1 = Contact("Ivan", "Telephone", "23street")
print(person1)