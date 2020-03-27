import re

booksArray = ['Preface  ', 'Genesis  ', 'Exodus  ', 'Leviticus  ', 'Numbers  ', 'Deuteronomy  ', 'Joshua  ', 'Judges  ', 'Ruth  ', '1 Samuel  ', '2 Samuel  ', '1 Kings  ', '2 Kings  ', '1 Chronicles  ', '2 Chronicles  ', 'Ezra  ', 'Nehemiah  ', 'Esther  ', 'Job  ', 'Psalms  ', 'Proverbs  ', 'Ecclesiastes  ', 'Song of Solomon  ', 'Isaiah  ', 'Jeremiah  ', 'Lamentations  ', 'Ezekiel  ', 'Daniel  ', 'Hosea  ', 'Joel  ', 'Amos  ', 'Obadiah  ', 'Jonah  ', 'Micah  ', 'Nahum  ', 'Habakkuk  ', 'Zephaniah  ', 'Haggai  ', 'Zechariah  ', 'Malachi  ', 'Tobit  ', 'Judith  ', 'Esther (Greek)  ', 'Wisdom of Solomon  ', 'Sirach  ', 'Baruch  ', '1 Maccabees  ', '2 Maccabees  ', '1 Esdras  ', 'Prayer of Manasses  ', 'Psalm 151  ', '3 Maccabees  ', '2 Esdras  ', '4 Maccabees  ', 'Daniel (Greek)  ', 'Matthew  ', 'Mark  ', 'Luke  ', 'John  ', 'Acts  ', 'Romans  ', '1 Corinthians  ', '2 Corinthians  ', 'Galatians  ', 'Ephesians  ', 'Philippians  ', 'Colossians  ', '1 Thessalonians  ', '2 Thessalonians  ', '1 Timothy  ', '2 Timothy  ', 'Titus  ', 'Philemon  ', 'Hebrews  ', 'James  ', '1 Peter  ', '2 Peter  ', '1 John  ', '2 John  ', '3 John  ', 'Jude  ', 'Revelation  ', 'Glossary  ']

bookCodeDict = {
    "Preface  ": "Pre",
    "Genesis  ": "Gen",
    "Exodus  ": "Exo",
    "Leviticus  ": "Lev",
    "Numbers  ": "Num",
    "Deuteronomy  ": "Deu",
    "Joshua  ": "Jos",
    "Judges  ": "Jud",
    "Ruth  ": "Rut",
    "1 Samuel  ": "1Sa",
    "2 Samuel  ": "2Sa",
    "1 Kings  ": "1Ki",
    "2 Kings  ": "2Ki",
    "1 Chronicles  ": "1Ch",
    "2 Chronicles  ": "2Ch",
    "Ezra  ": "Ezr",
    "Nehemiah  ": "Neh",
    "Esther  ": "Est",
    "Job  ": "Job",
    "Psalms  ": "Psa",
    "Proverbs  ": "Pro",
    "Ecclesiastes  ": "Ecc",
    "Song of Solomon  ": "SNG",
    "Isaiah  ": "Isa",
    "Jeremiah  ": "Jer",
    "Lamentations  ": "Lam",
    "Ezekiel  ": "EZK",
    "Daniel  ": "Dan",
    "Hosea  ": "Hos",
    "Joel  ": "JOL",
    "Amos  ": "Amo",
    "Obadiah  ": "Oba",
    "Jonah  ": "Jon",
    "Micah  ": "Mic",
    "Nahum  ": "NAM",
    "Habakkuk  ": "Hab",
    "Zephaniah  ": "Zep",
    "Haggai  ": "Hag",
    "Zechariah  ": "Zec",
    "Malachi  ": "Mal",
    "Tobit  ": "Tob",
    "Judith  ": "Jud",
    "Esther (Greek)  ": "Est",
    "Wisdom of Solomon  ": "Wis",
    "Sirach  ": "Sir",
    "Baruch  ": "Bar",
    "1 Maccabees  ": "1Ma",
    "2 Maccabees  ": "2Ma",
    "1 Esdras  ": "1Es",
    "Prayer of Manasses  ": "MAN",
    "Psalm 151  ": "Psa",
    "3 Maccabees  ": "3Ma",
    "2 Esdras  ": "2Es",
    "4 Maccabees  ": "4Ma",
    "Daniel (Greek)  ": "Dan",
    "Matthew  ": "Mat",
    "Mark  ": "MRK",
    "Luke  ": "Luk",
    "John  ": "JHN",
    "Acts  ": "Act",
    "Romans  ": "Rom",
    "1 Corinthians  ": "1Co",
    "2 Corinthians  ": "2Co",
    "Galatians  ": "Gal",
    "Ephesians  ": "Eph",
    "Philippians  ": "PHP",
    "Colossians  ": "Col",
    "1 Thessalonians  ": "1Th",
    "2 Thessalonians  ": "2Th",
    "1 Timothy  ": "1Ti",
    "2 Timothy  ": "2Ti",
    "Titus  ": "Tit",
    "Philemon  ": "PHM",
    "Hebrews  ": "Heb",
    "James  ": "JAS",
    "1 Peter  ": "1Pe",
    "2 Peter  ": "2Pe",
    "1 John  ": "1JN",
    "2 John  ": "2JN",
    "3 John  ": "3JN",
    "Jude  ": "Jud",
    "Revelation  ": "Rev",
    "Glossary  ": "Glo",
}


for book in booksArray:

    regex = re.compile("(^\S{3}|\d\s.{2})")
    rawBookCode = regex.match(book).group(0)
    bookCode = rawBookCode.replace(" ", "")

    # print("\"" + book + "\"" + ": " + "\"" + bookCode + "\",")

# # This code prints the url for chapter 1 of every book. It's useful for testing the URLs.
# for code in bookCodeDict.values():
#     print("https://www.bible.com/bible/206/" + code + ".1.WEB")

def getUrl(book, chapter):
    code = bookCodeDict[book]
    url = "https://www.bible.com/bible/206/" + code + "." + chapter + ".WEB"
    return url