import app.parser.ner as ner
import app.parser.getData as importArticles
import app.parser.chunker as chunker
import app.parser.traverser as traverser
articles = importArticles.getData()

for article in articles[0:5]:
    netdat = ner.NER(article[1])
    chunked = chunker.regexChunker(netdat)
    print traverser.traverse(chunked)
    print("--------------")
