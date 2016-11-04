import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import app.parser.getData as importArticles
import app.parser.articleRetrieval.getArticles as getContent
#import app.analytics.paragraphs as para
#import app.analytics.actionSentences as ac
#import app.analytics.stanford as sf
#import app.analytics.hasDate as hd
import app.parser.getChunks as gc
import app.analytics.tag as tag

articles = importArticles.getData()

sentences= []
count = 0
for article in articles[0:10]:
    chunks = gc.getChunks(article[1])
    tags =  tag.getTags(article[1],chunks)
    if tags == []:
        continue # check this is right. go to next itteration
    print tags
    """The Stanford Open IE tags"""
    subject = tags['subject']
    relation = tags['relation']
    objects = tags['object']

    #entities has [0] as objects and [1] as relations
    """wikiArticles =  getContent.getArticles(entities[0])
    try:
        for page in wikiArticles:#page = (entity,article)
            contextParagraphs = para.paragraphs(page, entities[0])
            for paragraph in contextParagraphs:
                if len(ac.getActionSentences(entities[1],paragraph)) > 0: sentences.append(ac.getActionSentences(entities[1],paragraph))
    except:
        pass
    #count =0
    if len(sentences) >0:
        for sentence in sentences:

            for item in sentence:
                sent = hd.hasDate(item)
                if(sent != False):
     #               count +=1
                    print "\n" + str(sent)
    #print count"""
