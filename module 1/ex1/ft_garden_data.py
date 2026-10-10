class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 2)
    plant2 = Plant("Tulip", 30, 1)
    plant3 = Plant("Daisy", 20, 3)

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()
