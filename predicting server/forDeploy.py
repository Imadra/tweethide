# deploy
import pickle
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

f = open('my_classifier.pickle', 'rb')
cls = pickle.load(f)
f.close()

stopwords_set = set(stopwords.words("english"))
w_features = open('words.txt', 'r').read().splitlines()


def extract_features(document):
    # document should be list
    document_words = set(document)
    features = {}
    for word in w_features:
        features['containts(%s)' % word] = (word in document_words)
    return features


def normSentenceTest(sentence):
    words_filtered = [e.lower() for e in sentence.split() if len(e) >= 2]
    words_cleaned = [word for word in words_filtered
                     if 'http' not in word
                     and not word.startswith('@')
                     and word != 'rt']
    words_without_stopwords = [re.sub('[^a-zA-Z]', '', word)
                               for word in words_cleaned if not word in stopwords_set]
    ps = PorterStemmer()
    words = [ps.stem(word) for word in words_without_stopwords]
    return words


def predict(sentence=''):
    sentence = sentence.lower()
    if ('world' in sentence and 'cup' in sentence) or 'wc2018' in sentence:  # hahahahahahahahahah
        return 'wc2018'
    sentence = normSentenceTest(sentence)
    res = cls.classify(extract_features(sentence))
    return res

