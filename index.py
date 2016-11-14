import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import app.parser.getData as importArticles
import app.parser.articleRetrieval.getArticles as getContent
import app.parser.getChunks as gc
import app.analytics.tag as tag
import app.parser.articleRetrieval.wikipediaParse as wp
import app.parser.sentences as sent
import app.analytics.sentenceFiltering.actionSentences as action
import app.analytics.functions.hasDate as hd
import app.analytics.functions.synonym as sn
import app.analytics.getFeatures as ft

articles = importArticles.getData()

sentences= []
count = 0
for article in articles[0:10]:
    print article
    chunks = gc.getChunks(article[1])
    tags =  tag.getTags(article[1],chunks)
    if tags == []:
        continue # check this is right. go to next itteration
    """The Stanford Open IE tags"""
    subject = tags['subject']
    relation = tags['relation']
    objects = tags['object']
    objects = objects.split()
    print objects
    print relation
    print subject

    article = wp.getArticle(subject)
    sentences = sent.getSentences(article)

    features= ft.getFeatures(subject, objects, relation, sentences)
