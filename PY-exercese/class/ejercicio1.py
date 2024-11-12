class Students:
    def __init__(self, name, years_old, grade):
        self.name = name
        self.years_old = years_old
        self.grade = grade

    def study(self):
        print(f"The student {self.name} is studying")

name = input("Enter your name: " )
years_old = input("Enter your years old: " )
grade = input("Enter your grade: " )

student1 = Students(name, years_old, grade)

print(f'''
    Student Information \n
    Name = {student1.name}
    years_old = {student1.years_old}
    grade = {student1.grade}
    ''')

student_study = input("Ocupation: ")
text = 'study'
while True:
    if student_study.lower() == text:
        student1.study()

