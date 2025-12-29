from game_data import data
from art import logo
import random

lose = False
score = 0

while not lose:
    print(f"\nYour current score is: {score}")

    a = random.choice(data)
    b = random.choice(data)

    while a == b:
        b = random.choice(data)

    print(f"A: {a['name']}, {a['description']}, from {a['country']}")
    print(logo)
    print(f"B: {b['name']}, {b['description']}, from {b['country']}")

    answer = input("Who do you think has more followers? (A/B): ").lower()

    if a["follower_count"] > b["follower_count"] and answer == "a":
        score += 1
        print("Correct! 🎉")
    elif b["follower_count"] > a["follower_count"] and answer == "b":
        score += 1
        print("Correct! 🎉")
    else:
        print("You Lose 😢")
        print(f"A had {a['follower_count']}M followers")
        print(f"B had {b['follower_count']}M followers")
        lose = True