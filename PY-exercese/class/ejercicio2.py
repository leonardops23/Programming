class A:
    pass

class B:
    def hello():
        print("Hello")

class C:
    def hello():
        print("Hello1")
    pass

class D:
    pass

class E:
    pass

class F(C, B):
    pass

person1 = F.hello()
