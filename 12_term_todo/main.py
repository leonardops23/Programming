
# todo app = es recomendable hacer clases no funciones

class TermTodo:
    def __init__(self):
        pass
    
    def show_terminal(self) -> None:
        return self.show_text

    def input_text() -> str:
        text_input = input(str("Ingrese su nombre: "))
        return text_input


user1 = TermTodo.input_text()
print(user1)
