class Plant:
    class _Statistics:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def add_grow(self) -> None:
            self._grow_count += 1

        def add_age(self) -> None:
            self._age_count += 1

        def add_show(self) -> None:
            self._show_count += 1

        def display(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, "
                  f"{self._show_count} show")

    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name

        if height < 0:
            print("Error: Height cannot be negative.")
            self._height = 0
        else:
            self._height = height

        if age < 0:
            print("Error: Age cannot be negative.")
            self._age = 0
        else:
            self._age = age

        self._stats = self._Statistics()

    def show(self) -> None:
        self._stats.add_show()
        print(f"{self._name}: {self._height}cm, "
              f"{self._age} days old")

    def grow(self, amount: int) -> None:
        if self._height + amount < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return

        self._height += amount
        self._stats.add_grow()

    def age(self, days: int) -> None:
        if self._age + days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return

        self._age += days
        self._stats.add_age()

    def set_height(self, height: int) ->None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return

        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return

        self._age = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def display_stats(self) -> None:
        self._stats.display(self._name)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 color: str):
        super().__init__(name, height, age)
        self._color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet.")


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int,
                 color: str, seeds: int = 0):
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class TreeStatistics():
        def __init__(self) -> None:
            self._shade_count = 0

        def add_shade(self) -> None:
            self._shade_count += 1

        def display(self, name: str) -> None:
            super().display(name)
            print(f"{self._shade_count} shade")

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = self.TreeStatistics()

    def produce_shade(self) -> None:
        self._stats.add_shade()

        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: "
              f"{round(self._trunk_diameter, 1)}cm")

    def display(self) -> None:
        


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self, days: int) -> None:
        if self._age + days < 0:
            super().age(days)
            return

        super().age(days)
        self._nutritional_value += days

    def grow(self, amount: int) -> None:
        if self._height + amount < 0:
            super().grow(amount)
            return

        super().grow(amount)
        self._nutritional_value += amount


def display_statistics(plant: 'Plant') -> None:
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("\n=== Check year-old ===")
    print(f"Is 30 days more than a year? "
          f"-> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? "
          f"-> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    display_statistics(flower)

    print("\n[asking the rose to grow and bloom]")
    flower.grow(8)
    flower.bloom()
    flower.show()
    display_statistics(flower)

    print("\n=== Tree")
    tree = Tree("Oak", 200, 365, 5.0)
    tree.show()
    display_statistics(tree)

    print("\n[asking the oak to produce shade]")
    tree.produce_shade()
    display_statistics(tree)

    print("\n=== Seed")
    seed = Seed("Sunflower", 80, 45, "yellow")
    seed.show()
    display_statistics(seed)

    print("\n[make sunflower grow, age and bloom]")
    seed.grow(30)
    seed.age(20)
    seed.bloom()
    seed.show()
    display_statistics(seed)

    print("\n=== Vegetable")
    vegetable = Vegetable("Tomato", 5, 10, "April")
    vegetable.show()

    print("\n[make tomato grow and age]")
    vegetable.grow(20)
    vegetable.age(20)
    vegetable.show()
    display_statistics(vegetable)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)
