from nltk import tokenize

def getSentences(article):
    sentences = tokenize.sent_tokenize(article)
    return sentences

