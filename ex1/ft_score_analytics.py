#!/usr/bin/env python3
import sys

def main() -> None:
    print("=== Player Score Analytics ===")
    argv: list[str] = sys.argv[1:]
    scores: list[int] = []

    for score in argv:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    if not scores:
        print(
        f"No scores provided. Usage: "
        f"python3 ft_score_analytics.py <score1>\n<score2> ..."
    )
        return

    Total_players: int = len(scores)
    Total_score: int = sum(scores)
    Average: float = Total_score / Total_players
    High: int = max(scores)
    Low: int = min(scores)
    Range: int = High - Low

    print(f"Total players: {Total_players}")
    print(f"Total score: {Total_score}")
    print(f"Average score: {Average}")
    print(f"High score: {High}")
    print(f"Low score: {Low}")
    print(f"Score range: {Range}")

if __name__ == "__main__":
    main()
