from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodone, Shiftling, Morphagon
class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass
    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodone()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()