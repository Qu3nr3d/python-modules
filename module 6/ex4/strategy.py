from abc import ABC, abstractmethod
from ex3.creatures import Creature, TransformCapability


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, entity: Creature):
        pass

    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self):
        self.name = "Normal"

    def is_valid(self, entity: Creature) -> bool:
        return True

    def act(self, entity: Creature):
        if self.is_valid(entity):
            print(entity.attack())





class AggressiveStrategy(BattleStrategy):
    def __init__(self):
        self.name = "Aggressive"

    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature):

        if self.is_valid(entity):
            print(entity.transform())
            print(entity.attack())
            print(entity.revert())
        else:
            raise StrategyError(f"Battle error, aborting tournament: Invalid Creature '{entity.name}' for this aggressive strategy")