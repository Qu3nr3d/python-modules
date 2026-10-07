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
        print(f"Plant created: {self.show()}")

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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 30, 10)
    plant1.set_height(25)
    plant1.set_age(30)
    print(plant1.show())
    plant1.set_height(-100)
    plant1.set_age(-100)
    print(f"Current state: {plant1.show()}")
