import random
import typing

print("=== Game Data Stream Processor ===")

names: list[str] = ["Andrea", "Marco", "Anna", "Pietro"]
actions: list[str] = ["kick", "punch", "run", "shoot"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name: str = random.choice(names)
        action: str = random.choice(actions)
        yield (name, action)


gen = gen_event()

for n in range(1000):
    name: str
    action: str
    name, action = next(gen)
    print(f"Event {n}: Player {name} did action {action}")

players_and_actions: list[tuple[str, str]] = []
for n in range(10):
    players_and_actions.append(next(gen))

print(f"Build list of 10 events: {players_and_actions}")


def consume_event(
    players_and_actions: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while players_and_actions:
        object = random.choice(players_and_actions)
        players_and_actions.remove(object)
        yield object


for event in consume_event(players_and_actions):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {players_and_actions}")
