from ex3 import FlameFactory, TransformCreatureFactory

def test_factory():
    print("Testing factory")
    fire = FlameFactory().create_base()
    print(fire.describe())
    print(fire.attack())
    fire_up = FlameFactory().create_evolved()
    print(fire_up.describe())
    print(fire_up.attack())
    print("\nTesting factory")
    normal = TransformCreatureFactory().create_base()
    print(normal.describe())
    print(normal.attack())
    normal_up = TransformCreatureFactory().create_evolved()
    print(normal_up.describe())
    print(normal_up.attack())

def test_battle():
    fire = FlameFactory().create_base()
    normal = TransformCreatureFactory().create_base()
    print("\nTesting battle")
    print(f"{fire.describe()}\n vs.\n{normal.describe()}\nfight!")
    print(fire.attack())
    print(normal.attack())

if __name__ == "__main__":
    test_factory()
    test_battle()