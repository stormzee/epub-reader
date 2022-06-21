

import logging
import ebooklib
from ebooklib import epub
import pyttsx3
from bs4 import BeautifulSoup


engine = pyttsx3.init()
voices = engine.getProperty('voices')
vce = [voice for voice in voices if voice.name == 'english_rp']

engine.setProperty('voice', vce)

# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume-0.8)
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-25)
# this should be the path to your epub file.
file_path = "/home/sammy/Downloads/cant hurt me master your mind and defy the odds_go.epub"

# read epub file like and get all chapters from epub file ...........
epubfile = epub.read_epub(file_path)
items = list(epubfile.get_items_of_type(ebooklib.ITEM_DOCUMENT))

# convert the chapters from html format into normal text, using bs4 
def chapter_to_text(chapter):
    epubhtml = BeautifulSoup(chapter.get_content(), 'html.parser') 
    text = [pgraph.get_text() for pgraph in epubhtml.find_all('p')]
    return ' '.join(text)


# chaptertexts = {}
# chapters = []
for chapt in items:
    chapt = chapter_to_text(chapt)
    # chaptertexts[chapt.get_name()] = chapter_to_text(chapt)
    # chapters.append(chapt)
    print(chapt)
    engine.say(chapt,'oppong')
    engine.runAndWait()
