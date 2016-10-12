import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import app.parser.chunkers.ner as ner
import app.parser.getData as importArticles
import app.parser.chunkers.chunker as chunker
import app.parser.chunkers.traverser as traverser
import app.analytics.entityFinder as EF
import app.parser.articleRetrieval.getArticles as getContent
import app.analytics.paragraphs as para
import app.analytics.actionSentences as ac
import app.parser.chunkers.stanford as sf

articles = importArticles.getData()

sentences= []
count = 0
for article in articles[0:10]:

    count = count +1
    print "%%%%"
    print article[1]
    netdata = ner.NER(article[1])
    chunked = chunker.regexChunker(netdata)
    titleList = traverser.traverse(chunked)
    entities = EF.entityFinder(titleList)
    try:
        stanford = sf.stanfordOpenIE(article[1])
        print entities
        print stanford['object']
        print stanford['relation']
        print stanford['subject']
    except:
        next
    #entities has [0] as objects and [1] as relations
    """wikiArticles =  getContent.getArticles(entities[0])
    try:
        for page in wikiArticles:#page = (entity,article)
            contextParagraphs = para.paragraphs(page, entities[0])
            for paragraph in contextParagraphs:
                if len(ac.getActionSentences(entities[1],paragraph)) > 0: sentences.append(ac.getActionSentences(entities[1],paragraph))
    except:
        pass
    print len(sentences)"""
#print len(sentences)/len(articles)
#print("--------------")
