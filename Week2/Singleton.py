class Dog:
    _instance = None

    def __init__(self, color, leg_length):
        self.color = color
        self.leg_length = leg_length

    def __new__(cls, color, leg_length):
        if not cls._instance:
            cls._instance = super(Dog, cls).__new__(cls)
            cls._instance.__init__(color, leg_length)
        return cls._instance

    @staticmethod
    def get_instance():
        if not Dog._instance:
            Dog._instance = Dog("Black", "Short")
        return Dog._instance


dog1 = Dog.get_instance()
print("Dog1", dog1.color, dog1.leg_length)
print("")

dog2 = Dog.get_instance()
dog2.color = "Brown"
dog2.leg_length = "Long"
print("Dog1", dog1.color, dog1.leg_length)
print("Dog2", dog2.color, dog2.leg_length)
