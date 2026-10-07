def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if 0 <= temp_int <= 40:
        return temp_int
    else:
        raise ValueError(f"Temperature {temp_int} is out of range (0-40)")


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp} st C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("Input data is '-50'")
    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("Input data is '100'")
    try:
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
