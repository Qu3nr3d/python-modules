from ex4 import *



def single_battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]):
    print("*** Tournament ***")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                entity1, strategy1 = opponents[i]
                entity2, strategy2 = opponents[j]

                print(entity1.describe())
                print("vs.")
                print(entity2.describe())
                print("now fight!")

                strategy1.act(entity1)
                strategy2.act(entity2)

    except StrategyError as e:
        print(e)
        return






if __name__ == "__main__":
    flame = FlameFactory().create_base()
    normal_up = TransformCreatureFactory().create_evolved()
    flame_up = FlameFactory().create_evolved()
    strategy = NormalStrategy()
    strategy_agg = AggressiveStrategy()
    single_battle([(flame, strategy), (normal_up, strategy_agg), (flame_up, strategy_agg)])
