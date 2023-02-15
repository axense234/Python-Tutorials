
class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)
    # Used to outright call the functions,useful in larger projects
    @classmethod
    def num_dogs(cls):
        return(len(cls.dogs))
    # When you wanna put a function in a class but really do not want to mess with the class itself
    @staticmethod
    def bark(n):
        # barks n times:
        for _ in range(n):
            print("Bark")


tim = Dog('Tim')
jim = Dog('Jim')