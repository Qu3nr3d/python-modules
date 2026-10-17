import random


def main() -> None:
    players = ["Alice", "bob", "Charlie", "dylan", "Emma"]
    existed_cap_players = [name for name in players if name.istitle()]
    cap_players = [name.capitalize() for name in players]
    print(f"\nInitial list of players: {players}")
    print(f"\nNew list with all names capitalized: {cap_players}")
    print(f"\nNew list of capitalized names only: {existed_cap_players}")
    scores = {player: random.randint(0, 100) for player in cap_players}
    print(f"\nScore dict: {scores}")
    avg = sum(scores.values()) / len(scores)
    print(f"\nScore average is {avg}")
    high_scores = {key: value for (key, value)
                   in scores.items() if value > avg}
    print(f"\nHigh scores: {high_scores}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    main()
