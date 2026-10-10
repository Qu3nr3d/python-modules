import random

achievements = {
    'Crafting Genius',
    'World Savior',
    'Master Explorer',
    'Collector Supreme',
    'Untouchable',
    'Boss Slayer',
    'Legendary Hero',
    'Treasure Hunter',
    'Speed Demon',
    'Shadow Walker',
    'Ultimate Survivor',
    'Quest Master',
    'Dungeon Conqueror',
    'Battle Prodigy',
    'Hidden Secrets',
    'Unstoppable Force',
    'Jack of All Trades',
    'Mythic Adventurer',
    'Perfectionist',
    'Rise of a Legend'
}


def gen_player_achievements():
    random_num: int = random.randint(4, 10)
    return set(random.sample(achievements, random_num))


if __name__ == "__main__":
    player1 = gen_player_achievements()
    player2 = gen_player_achievements()
    player3 = gen_player_achievements()
    player4 = gen_player_achievements()
    print(f"Player Alice: {player1}\n")
    print(f"Player Charlie: {player2}\n")
    print(f"Player Dylan: {player3}\n")
    print(f"Player Bob: {player4}\n")
    print("Common achievements:", set.intersection(
        player1, player2, player3, player4
    ))

    print("\nAlice unique achievements:",
          set.difference(player1, player2, player3, player4))
    print("\nCharlie unique achievements:",
          set.difference(player2, player1, player3, player4))
    print("\nDylan unique achievements:",
          set.difference(player3, player1, player2, player4))
    print("\nBob unique achievements:",
          set.difference(player4, player1, player2, player3))

    print("\nAlice is missing: ", set.difference(achievements, player1))
    print("\nCharlie is missing: ", set.difference(achievements, player2))
    print("\nDylan is missing: ", set.difference(achievements, player3))
    print("\nBob is missing: ", set.difference(achievements, player4))
