from abc import ABC, abstractmethod

class IHandler(ABC):
    @property
    @abstractmethod
    def successor(self):
        pass

    @successor.setter
    @abstractmethod
    def successor(self, successor):
        pass

    @abstractmethod
    def request_order(self, amount):
        pass

class MiniStorage(IHandler):
    def __init__(self):
        self._successor = None

    @property
    def successor(self):
        return self._successor

    @successor.setter
    def successor(self, successor):
        self._successor = successor

    def request_order(self, amount):
        if amount < 10:
            print(f"Mini storage: DONE!")
        else:
            print(f"Mini storage: Passed to Medium storage")
            self._successor.request_order(amount)

class MediumStorage(IHandler):
    def __init__(self):
        self._successor = None

    @property
    def successor(self):
        return self._successor

    @successor.setter
    def successor(self, successor):
        self._successor = successor

    def request_order(self, amount):
        if amount < 50:
            print(f"Medium storage: DONE!")
        else:
            print(f"Medium storage: Passed to Big storage")
            self._successor.request_order(amount)

class BigStorage(IHandler):
    def __init__(self):
        self._successor = None

    @property
    def successor(self):
        return self._successor

    @successor.setter
    def successor(self, successor):
        self._successor = successor

    def request_order(self, amount):
        if amount < 100:
            print(f"Big handler: DONE!")
        else:
            print(f"Big storage: Passed to Factory")
            self._successor.request_order(amount)

class FactoryHandler(IHandler):
    def __init__(self):
        self._successor = None

    @property
    def successor(self):
        return self._successor

    @successor.setter
    def successor(self, successor):
        self._successor = successor

    def request_order(self, amount):
        print(f"Factory: ((")

class ChainOfHandlers:
    def __init__(self):
        self._mini = MiniStorage()
        self._medium = MediumStorage()
        self._big = BigStorage()
        self._factory = FactoryHandler()

        self._mini.successor = self._medium
        self._medium.successor = self._big
        self._big.successor = self._factory

    def handle(self, amount):
        self._mini.request_order(amount)

if __name__ == "__main__":
    chain = ChainOfHandlers()
    amount = int(input("Enter quantity: "))
    chain.handle(amount)
