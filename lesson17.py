class dm:
    def displayinfo(self, name=''):
        print("Welcome to dynamic coding")
    
class majid(dm):
    def displayinfo(self):
        super().displayinfo()
        print("welcome majid")

obj=majid()
obj.displayinfo()
