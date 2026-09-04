import sys

class QuantityError(Exception):
    def __init__(self, message: str = "No scores provided") -> None:
        super().__init__(message)
        self.message: str = message


def count_len(argv: list) -> int:
    count: int = len(sys.argv) - 1
    if count <= 0:
        raise QuantityError
    return count

print("=== Player Score Analytics ===")

try:
    count: int = count_len(sys.argv)
    players: int = count
    i: int = 1
    scores: list[int] = []

    while count > 0:
        try:
            argv: int = (int(sys.argv[i]))
            scores.append(argv)
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")

        i = i + 1
        count = count - 1

        if not scores:
            raise QuantityError

    tot_score: int = sum(scores)
    average: float = tot_score / len(scores)
    high: int = max(scores)
    low: int = min(scores)
    score_range: int = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {players}")
    print(f"Total score: {tot_score}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")
except QuantityError as e:
    print(e)
