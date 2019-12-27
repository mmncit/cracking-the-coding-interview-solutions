class Dog:
    """A simple dog class"""
    def __init__(self):
        pass
    def speak(self):
        return "woof!"

    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """"returns the string food"""
        return "dog food!"

class PetStore:
    """Abstract factory"""

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(str(pet), "says", pet.speak())
        print(str(pet), "eats", pet_food)

factory = DogFactory()
shop = PetStore(factory)
shop.show_pet()

