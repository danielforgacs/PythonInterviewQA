def f1():
    print('A')

class C1:
    print('B')

    def __call__(self):
        print('C')

class M1(type):
    print('D')

    def __new__(cls, *args, **kwargs):
        print('E')
        return super().__new__(cls, *args, **kwargs)

class C3(metaclass=M1):
    print('F')

    def __init__(self):
        print('G')

def f2():
    print('H')

def f3():
    f1()
    C3()
    print('I')
    C1()()

c1 = C1()
c2 = C3()
f3()
