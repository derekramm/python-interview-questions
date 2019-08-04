
class MyBaseClass:
    def __init__(self, value):
        self.value = value

class A(MyBaseClass):
    def __init__(self, value):
        super(A, self).__init__(value)
        self.value *= 2


class B(MyBaseClass):
    def __init__(self, value):
        super(B, self).__init__(value)
        self.value += 5


class MyClass(A, B):
    def __init__(self, value):
        super(MyClass, self).__init__(value)


myclass = MyClass(5)
print(myclass.value)