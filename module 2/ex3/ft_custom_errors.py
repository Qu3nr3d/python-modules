class GardenError(Exception):
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error") -> None:
        super().__init__(message)


def check_tomato(temp:int) -> None:
    if temp > 40:
        raise PlantError("The tomato plant is wilting!")

def check_water(height:int) -> None:
    if height < 40:
        raise WaterError("Not enough water in the tank!")

def check_errors() -> None:
    print(f"Testing PlantError...")
    try:
        check_tomato(50)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("\n Testing WaterError...")
    try:
        check_water(20)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("\n Testing catching all garden errors...")
    try:
        check_tomato(100)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(20)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    check_errors()
    print("\nAll custom error types work correctly!")

