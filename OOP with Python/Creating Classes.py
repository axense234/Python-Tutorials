
class Dog(object):
    def __init__(self, name, age):
        # self - creating an attribute
        self.name = name
        self.age = age
        self.li = [1, 2, 3, 4]
        print("Nice ya made a dog!")

    def speak(self):
        print("Hi i am", self.name, "and i am", self.age, "years old!")

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight


tim = Dog("Tim", 3)
fred = Dog("Fred", 5)
tim.speak()
tim.change_age(5)
tim.add_weight(18)
tim.speak()
fred.speak()

print(tim.age)
print(tim.name)
print(fred.li)
