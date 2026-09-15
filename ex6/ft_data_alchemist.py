import random

print("=== Game Data Alchemist ===\n")

players_name: list[str] = ["Kevin", "lucas", "karen", "Hanna", "bob"]
print(f"Initial list of players: {players_name}\n")

all_capitalized: list[str] = [name.capitalize() for name in players_name]
print(f"New list with all names capitalized: {all_capitalized}\n")

originally_capitalized: list[str] = [
    name for name in players_name if name == name.capitalize()
]
print(f"New list of capitalized names only: {originally_capitalized}\n")

scores_dict: dict[str, int] = {
    name: random.randint(50, 100) for name in all_capitalized
}
print(f"Score dict: {scores_dict}")

average: float = sum(scores_dict.values()) / len(scores_dict)
print(f"Score average is {average}")
above_average_scores: dict[str, int] = {
    name: score for name, score in scores_dict.items() if score > average
}
print(f"High scores: {above_average_scores}")
