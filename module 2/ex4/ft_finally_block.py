class GardenError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message) -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

def test_watering_system(plants: list) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            try:
                water_plant(plant)
            except PlantError as e:
                print(f"Caught {e.__class__.__name__}: {e}")
                print("... ending tests and returning to main")
                return
    finally:
        print("Closing watering system\n")

if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    valid_plants: list = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants: list = ["Tomato", "lettuce", "Carrots"]
    print("Testing valid plants...")
    test_watering_system(valid_plants)
    print("Testing invalid plants...")
    test_watering_system(invalid_plants)
    print("Cleanup always happens, even with errors!")
