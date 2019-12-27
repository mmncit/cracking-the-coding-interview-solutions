class Borg:
    """Borg class making class attributes global"""
    _shared_state = {}  # attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state # make it an attribute dictionary

class Singleton(Borg): #Inherits from the Borg class
    """ This class now shares all its attributes among its various instances"""
    # This essentially makes the singleton object an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)

# Create a singleton object and add first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")

# print the object
print(x)

# Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.
y = Singleton(SNMP="Simple Network Management Protocol")

print(y)  # print the object