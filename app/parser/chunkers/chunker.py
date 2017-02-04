import nltk

def regexChunker(sentence):
    grammar = """NP:{<NNP>+}
                    {<NN>+}
                    {<NNP><NN>}
                 PERSON:{<PERSON>}
                      {<PERSON><ORGANISATION>}
                 PLACE: {<ORGANIZATION><NP>}
                 ORG:{<GPE><ORGANIZATION>}
                     {<ORGANIZATION>}
                     {<GPE><NP>}
                     {<GPE>}
                     {<JJ><NNP><NNP>}
                ACTION:{<VB|VBD|VBG|VBN|VBP|VBZ>}
"""
    chunked = nltk.RegexpParser(grammar)
    return chunked.parse(sentence)




