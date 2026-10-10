from sys import argv


if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")
    if len(argv) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(argv) - 1}")
        for i in range(len(argv) - 1):
            print(f"Argument {i + 1}: {argv[i + 1]}")
    print(f"Total arguments: {len(argv)}")
