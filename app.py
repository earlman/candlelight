import csv
import random
import re
from flask_qrcode import QRcode
from helpers import getUrl
from flask import Flask, render_template

bible = "bible.csv"

# Returns random line from bible


def randomVerse():
    
    # Get line from CSV
    with open(bible) as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
    
    # Parse line
    verse = {}
    verse["book"]   = chosen_row[0].decode('utf-8')
    verse["chNum"]  = chosen_row[1].decode('utf-8')
    verse["vNum"]   = chosen_row[2].decode('utf-8')
    verse["text"]   = chosen_row[3].decode('utf-8')
    
    # Create URL
    verse["url"]    = getUrl(verse["book"], verse["chNum"])

    return verse

def create_app():

    app = Flask(__name__)

    QRcode(app)

    @app.route('/')
    def home():
        return render_template('index.html',
            verse = randomVerse()
        )
    
    return app

create_app().run(debug=False)