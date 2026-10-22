from ex3 import TransformCreatureFactory

if __name__ == "__main__":
    normal = TransformCreatureFactory().create_base()
    print("Testing Creature with transform capability")
    print(f"base:\n{normal.describe()}")
    print(normal.attack())
    print(normal.transform())
    print(normal.attack())
    print(normal.revert())
    print("evolved:")
    normal_up = TransformCreatureFactory().create_evolved()
    print(normal_up.describe())
    print(normal_up.attack())
    print(normal_up.transform())
    print(normal_up.attack())
    print(normal_up.revert())