import glob
import pathlib
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def get_data():
    date = []
    mood_pos = []
    mood_neg = []
    for filename in glob.glob("diary\*.txt"):
        with open(filename, 'r') as file:
            # Reading content
            content = file.read()
            # Getting neg and pos moods value
            pos, neg = get_mood(content)
            mood_pos.append(pos)
            mood_neg.append(neg)
            # Got the date
            filepath = pathlib.Path(filename).name
            date.append(filepath.split('.')[0])
    return date, mood_pos, mood_neg


def get_mood(content):
    score = analyzer.polarity_scores(content)
    pos = score["pos"]
    neg = score["neg"]
    return pos, neg