import csv
import random
import re
from helpers import getUrl

bible = "bible.csv"

# Returns random line from bible


def randomLine():
    
    # Get line from CSV
    with open(bible) as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
    
    # Parse line
    verse = {}
    verse["book"]   = chosen_row[0]
    verse["chNum"]  = chosen_row[1]
    verse["vNum"]   = chosen_row[2]
    verse["text"]   = chosen_row[3]
    
    return verse



verse = randomLine()
print(getUrl(verse["book"], verse["chNum"]))
