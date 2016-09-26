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

for article in articles[0:1]:
    netdata = ner.NER(article[1])
    chunked = chunker.regexChunker(netdata)
    titleList = traverser.traverse(chunked)
    entities = EF.entityFinder(titleList)
    print entities[1]
    wikiArticles =  getContent.getArticles(entities[0])
    for page in wikiArticles:#page = (entity,article)
        contextParagraphs = para.paragraphs(page, entities[0])
        print len(contextParagraphs)
print("--------------")
