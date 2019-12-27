class Dog:
    """A simple dog class"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "woof!"

class Cat:
    """A simple dog class"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "meow!"

def get_pet(pet="dog"):
    """ The factory method to create object"""
    pets = dict(dog=Dog("hope"), cat=Cat("Peace"))
    # print(pets)
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())