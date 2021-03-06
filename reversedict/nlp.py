import nltk
try:
    packages = ['brown','conll2000','punkt','wordnet']
    map(nltk.download, packages)
except:
    pass

import textblob
import textblob.wordnet as wordnet

import stopwords
is_not_stopword = stopwords.get_is_not_stopword()

def lookup_word(term):
    return term if isinstance(term, textblob.Word) else textblob.Word(term)

def get_definitions_synonyms(term):
    word = lookup_word(term)
    synonyms = {l for s in word.get_synsets() for l in s.lemma_names()}
    return word.definitions, list(synonyms)

def join(*texts):
    return textblob.TextBlob('. ').join(texts)

def tokenize(text):
    blob = textblob.TextBlob(text) if not isinstance(text, textblob.TextBlob) else text
    return filter(is_not_stopword, blob.words)

def correct(text):
    return textblob.TextBlob(text).correct()
