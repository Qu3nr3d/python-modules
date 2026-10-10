from sys import argv

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(argv) == 1:
        print(f"No scores provided. Usage: {argv[0]} <score1> <score2> ...")
    else:
        try:
            argv[1:] = [int(x) for x in argv[1:]]
            print(f"Scores processed: {argv[1:]}")
            print(f"Total players: {len(argv[1:])}")
            print(f"Total score: {sum(argv[1:])}")
            print(f"Average score: {sum(argv[1:]) / len(argv[1:])}")
            print(f"High score: {max(argv[1:])}")
            print(f"Low score: {min(argv[1:])}")
            print(f"Score range: {max(argv[1:]) - min(argv[1:])}")
        except ValueError:
            for i in range(len(argv) - 1):
                try:
                    x: int = int(argv[i + 1])
                except ValueError:
                    print(f"Invalid Parameter: {argv[i + 1]}")
            print(f"No scores provided. Usage: {argv[0]}"
                  f" <score1> <score2> ...")
