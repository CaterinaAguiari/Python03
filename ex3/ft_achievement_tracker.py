import random


def generate_name_player() -> str:
    vowels: str = "aeiou"
    consonants: str = "bcdfghlmnpqrstvz"
    name: str = ""

    while len(name) < 6:
        name += random.choice(consonants) + random.choice(vowels)

    return name.capitalize()


ACHIEVEMENTS_LIST: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Unstoppable",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    num_achievements: int = random.randint(1, len(ACHIEVEMENTS_LIST))
    player_achievements: set[str] = set(
        random.sample(ACHIEVEMENTS_LIST, k=num_achievements)
    )
    return player_achievements


num_players: int = random.randint(4, 6)
players_data: list[tuple[str, set[str]]] = []

while len(players_data) < num_players:
    name: str = generate_name_player()
    achievements: set[str] = gen_player_achievements()
    players_data.append((name, achievements))

all_unlocked: set[str] = set()
shared_all: set[str] = players_data[0][1].copy()

idx: int = 0
while idx < len(players_data):
    current_set: set[str] = players_data[idx][1]
    all_unlocked = all_unlocked.union(current_set)
    shared_all = shared_all.intersection(current_set)
    idx += 1

print("=== Achievement Tracker System ===\n")

i: int = 0
while i < len(players_data):
    name_p, set_p = players_data[i]
    print(f"Player {name_p}: {set_p}")
    i += 1

print(f"\nAll distinct achievements: {all_unlocked}\n")
print(f"Common achievements: {shared_all}\n")

j: int = 0
while j < len(players_data):
    name_p, set_p = players_data[j]

    others_set: set[str] = set()
    other_idx: int = 0
    while other_idx < len(players_data):
        if other_idx != j:
            others_set = others_set.union(players_data[other_idx][1])
        other_idx += 1

    only_has: set[str] = set_p.difference(others_set)
    print(f"Only {name_p} has: {only_has}")
    j += 1
print()
all_possible: set[str] = set(ACHIEVEMENTS_LIST)
k: int = 0
while k < len(players_data):
    name_p, set_p = players_data[k]
    missing: set[str] = all_possible.difference(set_p)
    print(f"{name_p} is missing: {missing}")
    k += 1
