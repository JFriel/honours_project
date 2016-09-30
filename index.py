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
import app.analytics.actionSentences as ac
articles = importArticles.getData()

sentences= []
count = 0
for article in articles[0:100]:

    count = count +1
    print(str(count) + '/')
    print len(articles)
    print "%%%%"

    netdata = ner.NER(article[1])
    chunked = chunker.regexChunker(netdata)
    titleList = traverser.traverse(chunked)
    entities = EF.entityFinder(titleList)
    wikiArticles =  getContent.getArticles(entities[0])
    try:
        for page in wikiArticles:#page = (entity,article)
            contextParagraphs = para.paragraphs(page, entities[0])
            for paragraph in contextParagraphs:
                if len(ac.getActionSentences(entities[1],paragraph)) > 0: sentences.append(ac.getActionSentences(entities[1],paragraph))
    except:
        pass
    print len(sentences)
print len(sentences)/len(articles)
print("--------------")
