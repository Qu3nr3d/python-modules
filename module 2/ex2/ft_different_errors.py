def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
       x = 5 / 0
    elif operation_number == 2:
        directory = "/non/existent/file.txt"
        open(directory, "w")
    elif operation_number == 3:
        x = "abc" + 10
    else:
        print("Operation completed successfully")

def test_error_types():
    i:int = 0

    while i < 5:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
            print(f"Caught{e.__class__.__name__}: {e}")
        i += 1

if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
