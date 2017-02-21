import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import app.parser.getData as importArticles
import app.parser.articleRetrieval.getArticles as getContent
import app.parser.sentences as sent
import app.parser.getChunks as gc
import app.analytics.tag as tag
import app.parser.articleRetrieval.wikipediaParse as wp
import app.analytics.functions.hasDate as hd
import nltk
from multiprocessing import Pool
import pattern.en as en
data = open('data/train.txt','r').readlines()

for i in range(len(data)):
    data[i] = data[i].split(',')
#A

def getArticle(article):
    try:
        #chunks = gc.getChunks(article)
        tags =  tag.getTags(article[1])
        #if tags == []:
        try:
        #    continue # check this is right. go to next itteration
            """The Stanford Open IE tags"""
            subject = tags[-1]['subject']
            relation = tags[-1]['relation']
            objects = tags[-1]['object']
            objects = objects.split(' ')

            relations = []
            relations.append(nltk.stem.wordnet.WordNetLemmatizer().lemmatize(relation))
            relations = en.lexeme(relations[0])
            content = wp.getArticle(subject)
        except:
            #    continue # check this is right. go to next itteration
            """The Stanford Open IE tags"""
            subject = tags[0]['subject']
            relation = tags[0]['relation']
            objects = tags[0]['object']
            objects = objects.split(' ')
            relations = []
            relations.append(nltk.stem.wordnet.WordNetLemmatizer().lemmatize(relation))
            relations = en.lexeme(relations[0])
            content = wp.getArticle(subject)

        #objects = objects.split()
        rawSentences = nltk.tokenize.sent_tokenize(content)#sent.getSentences(content)
        sentences = []
        for sentence in rawSentences:
            for word in objects:
                if word in sentence:
                    sentences.append(sentence)
            for word in relations:
                if word in sentence:
                    sentences.append(sentence)

        sentences = list(set(sentences))
        return {'title':article[1], 'sentences':sentences, 'year':article[0]}
    except:
        return

p = Pool(25)
articleData = p.map(getArticle,data)
print articleData
"""
doubleSets = []
for I in range(0,len(articleData)):
    for J in range(I+1,len(articleData)):
        doubleSets.append((articleData[I], articleData[J]))
print doubleSets"""
