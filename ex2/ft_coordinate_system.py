import math
def get_player_pos() -> tuple[float, float, float]:
    while True:
        values = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            parts = values.split(",")
            count: int = 0
            x, y, z = "", "", ""

            for part in parts:
                if count == 0:
                    x = part
                elif count == 1:
                    y = part
                elif count == 2:
                    z = part
                count = count + 1
            
            if count != 3:
                raise ValueError("You must provide exactly 3 coordinates.")

            x = float(x.strip())
            y = float(y.strip())
            z = float(z.strip())

            return x, y, z

        except ValueError as e:
            print(f"Invalid intput: {e}. Try again!")