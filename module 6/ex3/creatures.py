from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self):
        pass

    def describe(self):
        return f'{self.name} is a {self.type} Creature'


class TransformCapability(ABC):
    @abstractmethod
    def transform(self):
        pass
    @abstractmethod
    def revert(self):
        pass

class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self):
        return f"{self.name} uses Ember!"


class Pyrodone(Creature):
    def __init__(self):
        super().__init__("Pyrodone", "Fire/Flying")

    def attack(self):
        return f"{self.name} attacks {self.type}"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        self.transformed = False

    def attack(self):
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self):
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self):
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        self.transformed = False

    def attack(self):
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self):
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self):
        self.transformed = False
        return f"{self.name} stabilizes its form."


