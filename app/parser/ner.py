import nltk

def NER(sentence):
    try:
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        entities = nltk.ne_chunk(tagged)
        return entities;
    except:
        print "Something went wrong"

