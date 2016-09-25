import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import app.parser.ner as ner
import app.parser.getData as importArticles
import app.parser.chunker as chunker
import app.parser.traverser as traverser
import app.analytics.entityFinder as EF
import app.parser.getArticles as getContent
import app.analytics.paragraphs as para
articles = importArticles.getData()

for article in articles[0:5]:
    paras = []
    print article
    print '\n'
    netdat = ner.NER(article[1])
    chunked = chunker.regexChunker(netdat)
    titleList = traverser.traverse(chunked)
    entities = EF.entityFinder(titleList)
    articles =  getContent.getArticles(entities[0])
    print len(para.paragraphs(articles[0], entities[0]))
    print("--------------")
