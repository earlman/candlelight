# Creates bible.csv for use in application

import csv
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


def parseXML(xmlfile):

    # create empty list for verses
    verses = []

    # create soup
    with open(xmlfile) as fp:
        soup = BeautifulSoup(fp, 'xml')

    # find w:r tags
    wr = soup.find_all('w:r')

    # iterate w:r items
    for x in wr:

        # check if w:r is a 'cvmarker'
        if (x.find("w:rStyle", attrs={"w:val": "cvmarker"})):

            # Build verse dictionary using buildVerse()
            verse = buildVerse(x)

            # Append verse to list if text exists (otherwise skip)
            if verse:
                verses.append(verse)

    return verses


def buildVerse(cvmarker):
    # empty verse dictionary
    verse = {}

    # append chapter number to the list
    verse['chNum'] = cvmarker.find("w:t").contents[0].encode('utf8')

    # add verse number to list
    vnum_ref = cvmarker.next_sibling
    verse['vNum'] = vnum_ref.find(
        "w:t").contents[0].encode('utf8')

    # add verse text to list
    verse_ref = vnum_ref.next_sibling
    if verse_ref:
        verse['text'] = verse_ref.contents[0].text.encode('utf8')
    else:
        # return empty
        return None

    return verse


def savetoCSV(verses, filename):

    # specifying the fields for csv file
    fields = ['chNum', 'vNum', 'text']

    # writing to csv file
    with open(filename, 'w') as csvfile:

        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(verses)


def main():

    # url of xml
    fileUrl = 'C:/Projects/bible (python)/eng-web_word/eng-web_word.xml'
    # fileUrl = 'C:/Projects/bible (python)/samplerssfeed.xml'

    # parse xml file
    verses = parseXML(fileUrl)

    # print(verses)

    # store news items in a csv file
    savetoCSV(verses, 'bible.csv')


if __name__ == "__main__":

    # calling main function
    main()
