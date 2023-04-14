from flask import Flask, request, render_template
import nltk
from nltk.corpus import cmudict
nltk.download('cmudict')
d = cmudict.dict()

app = Flask(__name__)

def get_first_syllable(word):
    try:
        syllables = [list(y for y in x if y[-1].isdigit()) for x in d[word.lower()]][0]
        first_syllable = ''.join([syl[:-1] for syl in syllables])
        return first_syllable
    except KeyError:
        return word

text= "Hello"
words = text.split()
result = ''
for word in words:
    first_syllable = get_first_syllable(word)
    print(first_syllable)
    result += f'<b>{first_syllable}</b>{word[len(first_syllable):]} '
