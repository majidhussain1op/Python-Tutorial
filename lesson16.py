class Student:
    def __init__(self, name, roll_no):
        self.__name = name  # private attribute
        self.__roll_no = roll_no

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if len(new_name) > 0:
            self.__name = new_name
        else:
            print("Invalid name!")

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, new_roll_no):
        if isinstance(new_roll_no, int) and new_roll_no > 0:
            self.__roll_no = new_roll_no
        else:
            print("Invalid Roll Number!")


student1 = Student("Zara", 100)


print("Name:", student1.get_name())
print("Roll No:", student1.get_roll_no())


student1.set_name("Aisha")
student1.set_roll_no(200)

# Accessing updated values
print("Updated Name:", student1.get_name())
print("Updated Roll No:", student1.get_roll_no())
