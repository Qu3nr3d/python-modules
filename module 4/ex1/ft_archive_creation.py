from sys import argv


def main():
    if len(argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    file_name = argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        file = open(file_name)
        data = file.read()
        file.close()
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    print("---")
    print(data, end="")
    print("\n---")
    print(f"File '{file_name}' closed.")

    part_2(data)


def part_2(data):
    transformed_data = ""

    for char in data:
        if char == "\n":
            transformed_data += "#\n"
        else:
            transformed_data += char

    if len(data) > 0 and data[-1] != "\n":
        transformed_data += "#"

    print("\nTransform data:")
    print("---")
    print(transformed_data)

    new_file_name = input("Enter new file name (or empty): ")

    if new_file_name:
        try:
            new_file = open(new_file_name, "w")
            new_file.write(transformed_data)
            new_file.close()

            print(f"Data saved in file '{new_file_name}'.")
        except OSError as e:
            print(f"Error saving file '{new_file_name}': {e}")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()