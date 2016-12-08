import collections, re
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import operator
import functions.hasDate as hd
def preprocessor(data):
    return " ".join([SnowballStemmer("english").stem(word) for word in data.split()])

def getWords(sentence):
    returnWords = []
    words = re.findall(r'\w+', sentence.lower())
    for w in words:
        if w not in stopwords.words('english'):
            returnWords.append(w)
    return returnWords

def bagOfWordsDict(texts):
    #vectorizer = CountVectorizer(preprocessor=preprocessor).fit(texts)
    #bagOfWords = vectorizer.vocabulary_
    #sorted_bagOfWords = sorted(bagOfWords.items(), key=operator.itemgetter(1))
    #return sorted_bagOfWords

    bagsofwords = [ collections.Counter(getWords(txt)) for txt in texts]
    #bagsofwords = [w for w in bagsofwords if not w in stopwords.words("english")]
    filtered_words = [word for word in bagsofwords if word not in stopwords.words('english')]
    sumbags = sum(filtered_words, collections.Counter())
    return sumbags

def bagOfWordsList(sentences):
    words = []
    for sentence in sentences:
        if(hd.hasDate(sentence) != []):
            words.append(getWords(sentence))
    return set(words)

def featureExtraction(sentences):
    bow = bagOfWordsDict(sentences)
    #bow = bagOfWordsList(sentences)
    return bow


