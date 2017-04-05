import sys
import theano
import numpy

reload(sys)
sys.setdefaultencoding('utf-8')
P1 = "Kevin James Schuler (born 11 March 1967) is a New Zealand rugby union coach and former rugby union player. A flanker, Schuler represented Manawatu and North Harbour at a provincial level, and was a member of the New Zealand national side, the All Blacks, between 1989 and 1995. He played 13 matches for the All Blacks including four internationals. He moved to Japan in 1996 and played for Yamaha Jubilo, where he became player-coach and later head coach. He has also had coaching roles with Bay of Plenty and the Chiefs in New Zealand."
P2 = "The story, written by Yolen,is told in present tense from the a third person point of view (a third person narrative) and takes the form of a short story of 32 pages. A lot of this story is centralized upon the daughter and how everyone's opinion changes once the daughter does something amazing. The illustrations by Young, which also precede and follow the text, include a very detailed and traditional style of art that follows very closely to the actions that are being presented in the text."

"""
nh :: dimension of the hidden layer
        nc :: number of classes
        ne :: number of word embeddings in the vocabulary
        de :: dimension of the word embeddings
        cs :: word window context size 
"""
nh=1
nc=2
ne=7
de=2
cs=7

emb = theano.shared(0.2 * numpy.random.uniform(-1.0, 1.0,\
                   (ne+1, de)).astype(theano.config.floatX)) # add one for PADDING at the end

vocab = []
for w in P1.split():
    if w not in vocab:
        vocab.append(w)
for w in P2.split():
    if w not in vocab:
        vocab.append(w)

sentence1 = []
for w in P1.split():
    sentence1.append(vocab.index(w))

sentence2 = []
for w in P2.split():
    sentence2.append(vocab.index(w))


def contextwin(l, win):
    '''
    win :: int corresponding to the size of the window
    given a list of indexes composing a sentence

    l :: array containing the word indexes

    it will return a list of list of indexes corresponding
    to context windows surrounding each word in the sentence
    '''
    assert (win % 2) == 1
    assert win >= 1
    l = list(l)

    lpadded = win // 2 * [-1] + l + win // 2 * [-1]
    out = [lpadded[i:(i + win)] for i in range(len(l))]

    assert len(out) == len(l)
    return out

import theano, numpy
from theano import tensor as T

# nv :: size of our vocabulary
# de :: dimension of the embedding space
# cs :: context window size
nv, de, cs = 1000, 50, 5

embeddings = theano.shared(0.2 * numpy.random.uniform(-1.0, 1.0, \
    (nv+1, de)).astype(theano.config.floatX)) # add one for PADDING at the end

idxs = T.imatrix() # as many columns as words in the context window and as many lines as words in the sentence
x = emb[idxs].reshape((idxs.shape[0], de*cs))


sentence1c = contextwin(sentence1,7)

f = theano.function(inputs=[idxs], outputs=x)
print f(sentence1c)
print f(sentenc1c).shape
