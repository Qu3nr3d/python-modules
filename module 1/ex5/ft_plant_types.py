class Plant():
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        if height < 0:
            print("Error: Height cannot be negative.")
            self._height = 5
        else:
            self._height = height
        if age < 0:
            print("Error: Age cannot be negative.")
            self._age = 0
        else:
            self._age = age

    def show(self):
        return f"{self._name}: {self._height}cm, {self._age} days old"

    def set_age(self, age: int):
        if age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age

    def set_height(self, height: int):
        if height < 0:
            print(f"{self._name.capitalize()}: "
                  f"Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def age(self, days: int):
        self._age += days

    def grow(self, growth: int):
        self._height += growth


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._has_bloomed = False

    def bloom(self):
        self._has_bloomed = True

    def show(self):
        print("=== Flower")
        print(super().show())
        print(f"Color: {self.color}")
        if self._has_bloomed:
            print(f"{self._name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self._name.capitalize()} has not bloomed yet.")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of {self._height}cm "
              f"long and {self._trunk_diameter}cm wide.")

    def show(self):
        print("=== Tree")
        print(super().show())
        print(f"Trunk Diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self):
        print("=== Vegetable")
        print(super().show())
        print(f"Harvest Season: {self._harvest_season}")
        print(f"Nutritional Value: {self._nutritional_value}")

    def age(self, days: int):
        super().age(days)
        self._nutritional_value += days

    def grow(self, growth: int):
        super().grow(growth)
        self._nutritional_value += growth


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    flower = Flower("Rose", 25, 2, "Red")
    flower.show()
    flower.bloom()
    flower.show()

    tree = Tree("Oak", 100, 5, 30.0)
    tree.show()
    tree.produce_shade()

    vegetable = Vegetable("Carrot", 15, 1, "Spring")
    vegetable.show()
    vegetable.grow(20)
    vegetable.age(10)
    vegetable.show()
