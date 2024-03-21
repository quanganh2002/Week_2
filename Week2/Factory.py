from abc import ABC, abstractmethod

# Abstract Product
class Dog(ABC):
    @abstractmethod
    def dog_color(self):
        pass

# Concrete Products
class BlackDog(Dog):
    def __init__(self):
        self.color = "Black"

    def dog_color(self):
        return self.color

class BrownDog(Dog):
    def __init__(self):
        self.color = "Brown"

    def dog_color(self):
        return self.color

# Factory
class Factory:
    class DogType:
        BlackDog, BrownDog = 0, 1

    def ColorDog(self, _color):
        color = None
        if _color == self.DogType.BlackDog:
            color = BlackDog()
        elif _color == self.DogType.BrownDog:
            color = BrownDog()
        return color

# Client
if __name__ == "__main__":
    _color = Factory.DogType.BrownDog
    color_factory = Factory()

    if _color == Factory.DogType.BlackDog:
        color = BlackDog()
    else:
        color = BrownDog()

    print(color.dog_color())

    color = color_factory.ColorDog(_color)
    print(color.dog_color())
