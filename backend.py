import glob
import pathlib
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def get_data():
    date = []
    pos = []
    neg = []
    for filename in glob.glob("diary\*.txt"):
        with open(filename, 'r') as file:
            # Reading content
            content = file.read()
            # Getting neg and pos moods value
            score = analyzer.polarity_scores(content)
            pos.append(score["pos"])
            neg.append(score["neg"])
            # Got the date
            filepath = pathlib.Path(filename).name
            date.append(filepath.split('.')[0])
    return date, pos, neg