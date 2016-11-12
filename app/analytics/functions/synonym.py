from nltk.corpus import wordnet as wn

#for synset in wn.synsets('dog'):
 #   for lemma in synset.lemmas():
  #      print lemma.name()


def synonym(word):
    synonyms = []
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
    return synonyms
