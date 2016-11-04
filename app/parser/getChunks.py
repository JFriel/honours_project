import chunkers.ner as ner
import chunkers.chunker as chunker
import chunkers.traverser as traverser

#takes a list [0,1]
def getChunks(articleTitle):
    nerData = ner.NER(articleTitle)
    chunkedData = chunker.regexChunker(nerData)
    titleList = traverser.traverse(chunkedData)
    return titleList
