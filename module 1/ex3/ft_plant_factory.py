class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age_days = age
        print(f"Created: {self.show()}")

    def show(self):
        return f"{self.name}: {self.height}cm, {self.age_days} days old"

    def age(self, days: int):
        self.age_days += days

    def grow(self, growth: int):
        self.height += growth


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 2),
        Plant("Tulip", 30, 1),
        Plant("Daisy", 20, 3),
        Plant("Sunflower", 15, 0),
        Plant("Orchid", 10, 5)
    ]
