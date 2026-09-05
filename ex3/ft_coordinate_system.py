import math
def get_player_pos() -> tuple[float, float, float]:
    while True:
        values: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            parts = values.split(",")
            x, y, z = parts

        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x_clean: str = x.strip()
            x: float = float(x_clean)
        except ValueError as e:
            print(f"Error on parameter '{x_clean}': {e}")
            continue

        try:
            y_clean: str = y.strip()
            y: float = float(y_clean)
        except ValueError as e:
            print(f"Error on parameter '{y_clean}': {e}")
            continue

        try:
            z_clean: str = z.strip()
            z: float = float(z_clean)
        except ValueError as e:
            print(f"Error on parameter '{z_clean}': {e}")
            continue

        return (x, y, z)

print("=== Game Coordinate System ===\n")
print("Get a first set of coordinates")
pos1: tuple[float, float, float] = get_player_pos()
print(f"Got a first tuple: {pos1}")
print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
dist_to_center: float = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
print(f"Distance to center: {round(dist_to_center, 4)}\n")
print("Get a second set of coordinates")
pos2: tuple[float, float, float] = get_player_pos()
dist_between: float = math.sqrt(
    (pos2[0] - pos1[0])**2 + 
    (pos2[1] - pos1[1])**2 + 
    (pos2[2] - pos1[2])**2
)
print(f"Distance between the 2 sets of coordinates: {round(dist_between, 4)}")