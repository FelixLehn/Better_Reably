from flask import Flask, request, render_template
import spacy
from spacy_syllables import SpacySyllables
import contractions


nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("syllables", after="tagger")

app = Flask(__name__)

def expand_contractions(text):
    expanded_text = contractions.fix(text)
    return expanded_text

def get_first_syllable(word):
    try:
        doc = nlp(word)

        first_syllable = [token._.syllables[0] for token in doc if token.is_alpha][0]
        return first_syllable
    except KeyError:
        return word

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        text = expand_contractions(text)
        words = text.split()
        result = ''
        for word in words:
            first_syllable = get_first_syllable(word)
            result += f'<b>{first_syllable}</b>{word[len(first_syllable):]} '
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()