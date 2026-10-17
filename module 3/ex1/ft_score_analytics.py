from sys import argv

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(argv) == 1:
        print(f"No scores provided. Usage: {argv[0]} <score1> <score2> ...")
    else:
        try:
            nums: list[int] = [int(x) for x in argv[1:]]
            print(f"Scores processed: {nums[:]}")
            print(f"Total players: {len(nums[:])}")
            print(f"Total score: {sum(nums[:])}")
            print(f"Average score: {sum(nums[:]) / len(nums[:])}")
            print(f"High score: {max(nums[:])}")
            print(f"Low score: {min(nums[:])}")
            print(f"Score range: {max(nums[:]) - min(nums[:])}")
        except ValueError:
            for i in range(len(argv) - 1):
                try:
                    x: int = int(argv[i + 1])
                except ValueError:
                    print(f"Invalid Parameter: {argv[i + 1]}")
            print(f"No scores provided. Usage: {argv[0]}"
                  f" <score1> <score2> ...")
