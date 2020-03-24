import csv
import random

bible = "bible.csv"

# Returns random line from bible


def randomLine():
    with open(bible) as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
    return chosen_row


print(randomLine())
print(randomLine())
print(randomLine())
print(randomLine())
