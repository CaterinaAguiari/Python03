import random
def genera_nome_giocatore() -> str:
    vocali: str = "aeiou"
    consonanti: str = "bcdfghlmnpqrstvz"
    nome: str = ""

    while len(nome) < 6:
        nome += random.choice(consonanti) + random.choice(vocali)

    return nome.capitalize()

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

num_giocatori: int = random.randint(4, 6)
dati_giocatori: list[tuple[str, set[str]]] = []

while len(dati_giocatori) < num_giocatori:
    nome: str = genera_nome_giocatore()
    achievements: set[str] = gen_player_achievements()
    dati_giocatori.append((nome, achievements))

all_unlocked: set[str] = set()
shared_all: set[str] = dati_giocatori[0][1].copy()

idx: int = 0
while idx < len(dati_giocatori):
    current_set: set[str] = dati_giocatori[idx][1]
    all_unlocked = all_unlocked.union(current_set)
    shared_all = shared_all.intersection(current_set)
    idx += 1

print("=== Achievement Tracker System ===\n")

# Stampa i set di ciascun giocatore
i: int = 0
while i < len(dati_giocatori):
    nome_p, set_p = dati_giocatori[i]
    print(f"Player {nome_p}: {set_p}")
    i += 1

print(f"\nAll distinct achievements: {all_unlocked}\n")
print(f"Common achievements: {shared_all}\n")

j: int = 0
while j < len(dati_giocatori):
    nome_p, set_p = dati_giocatori[j]

    others_set: set[str] = set()
    other_idx: int = 0
    while other_idx < len(dati_giocatori):
        if other_idx != j:
            others_set = others_set.union(dati_giocatori[other_idx][1])
        other_idx += 1

    only_has: set[str] = set_p.difference(others_set)
    print(f"Only {nome_p} has: {only_has}")
    j += 1
print()
all_possible: set[str] = set(ACHIEVEMENTS_LIST)
k: int = 0
while k < len(dati_giocatori):
    nome_p, set_p = dati_giocatori[k]
    missing: set[str] = all_possible.difference(set_p)
    print(f"{nome_p} is missing: {missing}")
    k += 1