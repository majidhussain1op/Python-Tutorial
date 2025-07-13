class SelfClass:
    def __init__(self):
        print("Welcome to Dynamic Coding with Majid")

    a=20

    def showValue(self):
        self.c=self.a+self.a
        print(self.c)

obj=SelfClass()
obj.showValue()