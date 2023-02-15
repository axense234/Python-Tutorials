
class Dog(object):
    def __init__(self, name, age):
        # self - creating an attribute
        self.name = name
        self.age = age

    def speak(self):
        print("Hi i am", self.name, "and i am", self.age, "years old!")

    def talk(self):
        print("Bark!")


class Cat(Dog):
    def __init__(self, name, age, color):
        # -supper(called the initialization of the supper class,in this case, Dog)
        super().__init__(name, age)
        self.color = color
    # -overwriting a function
    def talk(self):
        print("Meow")

tim = Cat("Tim", 5, "Blue")
tim.speak()
tim.talk()