import nltk

def NER(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.ne_chunk(tagged)
    return entities;

