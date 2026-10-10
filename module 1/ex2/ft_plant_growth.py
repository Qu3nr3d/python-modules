class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def age(self, days: int) -> None:
        self.age_days += days

    def grow(self, growth: float) -> None:
        self.height += growth


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 2)
    start_height = plant1.height

    print("=== Garden Plant Growth ===")
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        plant1.age(1)
        plant1.grow(0.8)
        print(f"{plant1.name}: {plant1.height}cm, {plant1.age_days} days old")
    print(f"Growth this week: {round(plant1.height - start_height, 1)} cm")
