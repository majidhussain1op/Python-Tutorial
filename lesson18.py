class A:
    def showData(self):
        print("I have passing of grade A")

class B(A):
    def showData(self):
        print("i have passing marks of B grade")

obj=B()
obj.showData()