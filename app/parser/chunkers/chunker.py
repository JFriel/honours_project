import nltk

def regexChunker(sentence):
    grammar = """NP:{<NNP>+}
                    {<NN>+}
                    {<NNP><NN>}
                 PLACE: {<ORGANIZATION><NP>}
                 ORG:{<GPE><ORGANIZATION>}
                     {<GPE><NP>}
                     {<GPE>}
                ACTION:{<VB|VBD|VBG|VBN|VBP|VBZ>}
"""
    chunked = nltk.RegexpParser(grammar)
    return chunked.parse(sentence)




