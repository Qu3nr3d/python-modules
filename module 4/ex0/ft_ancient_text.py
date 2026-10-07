from sys import argv


def main():
    if len(argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name = argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file: {file_name}")

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


if __name__ == "__main__":
    main()