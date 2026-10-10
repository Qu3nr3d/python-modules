from math import sqrt


def get_player_pos():
    while True:
        coordinates: str = str(input("Enter new coordinates"
                                     " as floats in format 'x,y,z': "))
        x = ""
        y = ""
        z = ""
        current = 0
        commas = 0

        for c in coordinates:
            if c == ",":
                current += 1
                commas += 1
            elif current == 0:
                x += c
            elif current == 1:
                y += c
            else:
                z += c

        if commas != 2:
            print("Invalid syntax")
            continue

        try:
            x = float(x)
        except ValueError:
            print(f"Error on parameter '{x}':"
                  f" could not convert string to float: '{x}'")
            continue

        try:
            y = float(y)
        except ValueError:
            print(f"Error on parameter '{y}':"
                  f" could not convert string to float: '{y}'")
            continue

        try:
            z = float(z)
        except ValueError:
            print(f"Error on parameter '{z}':"
                  f" could not convert string to float: '{z}'")
            continue

        return x, y, z


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first = get_player_pos()

    center = sqrt(
        (0 - first[0])**2 +
        (0 - first[1])**2 +
        (0 - first[2])**2
    )

    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    print(f"Distance to center: {round(center, 4)}")

    print("Get a second set of coordinates")
    second = get_player_pos()

    distance = sqrt(
        (second[0] - first[0])**2 +
        (second[1] - first[1])**2 +
        (second[2] - first[2])**2
    )

    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")
