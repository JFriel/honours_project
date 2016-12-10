import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import app.parser.getData as importArticles
import app.parser.articleRetrieval.getArticles as getContent
import app.parser.sentences as sent
import app.parser.getChunks as gc
import app.analytics.tag as tag
import app.parser.articleRetrieval.wikipediaParse as wp
import app.analytics.features as fe
import app.analytics.functions.hasDate as hd
import app.analytics.filterSentences as fl
from sklearn import tree, feature_extraction
from sklearn.feature_extraction.text import CountVectorizer
from multiprocessing import Pool
import numpy as np
import datetime

import networkx as nx
import matplotlib.pyplot as plt


np.seterr(divide='ignore',invalid='ignore')

trainArticles= open('singleShort.txt','r').readlines()#=importArticles.getData('train')
testArticles = open('singleShortTest.txt','r').readlines()#= importArticles.getData('test')
print len(trainArticles)
print len(testArticles)
listOfYears = []


testArticleLookupDict = {}
for title in range(0,len(testArticles)):
    print (eval(testArticles[title])['title'])
    testArticleLookupDict[eval(testArticles[title])['title']] = title

clf = tree.DecisionTreeClassifier()
titles = []
weights = []

#G = nx.Graph()#G is an empty graph


#A
def getArticle(article):
    singleSets = []
    try:
        chunks = gc.getChunks(article[1])
        tags =  tag.getTags(article[1],chunks)
        #if tags == []:
        #    continue # check this is right. go to next itteration
        """The Stanford Open IE tags"""
        subject = tags['subject']
        relation = tags['relation']
        objects = tags['object']
        objects = objects.split()

        content = wp.getArticle(subject)
        rawSentences = sent.getSentences(content)
        sentences = []
        for sentence in rawSentences:
            if(hd.hasDate(sentence) != []):
                sentences.append(sentence)
        listOfYears.append(article[0])
        SS = {'title':article[1], 'sentences':sentences, 'year':article[0]}
        singleSets.append(SS)
    except:
        pass
    return singleSets


#B
def generateTrainDataPoints(tpl):
    X = tpl[0]
    Y = tpl[1]
    doubleSets = []
    I = eval(trainArticles[X])
    J = eval(trainArticles[Y])
    sentencesI = fl.filter(I['sentences'],I['title'])
    sentencesJ = fl.filter(J['sentences'],J['title'])
    if(I['year'] < J['year']):
        b = 1
    else:
        b = 0
    val = ({'title1':I['title'],'sentences1':sentencesI,\
            'title2':J['title'],'sentences2': sentencesJ,\
            'year':b, 'vocab':set(sentencesI + sentencesJ)})
    return val
def generateTestDataPoints(tpl):
    X = tpl[0]
    Y = tpl[1]
    doubleSets = []
    I = eval(testArticles[X])
    J = eval(testArticles[Y])
    if(I['year'] < J['year']):
        b = 1
    else:
        b = 0
    val = ({'title1':I['title'],'sentences1':I['sentences'],\
            'title2':J['title'],'sentences2': J['sentences'],\
            'year':b, 'vocab':set(I['sentences'] + J['sentences'])})
    return val

def getFeature(item):
    yr = item['year']
    vec = fe.get(item['sentences1'],item['sentences2'])
    titles = ([item['title1'],item['title2']])
    return ([vec,titles,yr])
#C
def train(features):
    X = [item[0] for item in features]
    Y = [item[2] for item in features]
    clf.fit(X,Y)


def test(features):
    correct = 0
    for feature in features:
        predict = clf.predict(np.array([feature[0]]))
        prob = clf.predict_proba(np.array([feature[0]]))
        #prob = prob[0][predict][0]
        title1 = feature[1][0]
        title2 = feature[1][1]
        #print "title1 = " + str(title1)
        print prob
        #print str(title1) + "," + str(title2) + "," + str(float(prob))
        #G.add_edge(str(title1),str(title2), weight=float(prob)*1000)
        if(feature[2] == predict):
            correct +=1
    print "Accuracy = " + str(correct) + '/' + str(len(features))

#def tsp():



print datetime.datetime.now()
p = Pool(10)
#Used to get Article Content
#articles = (p.map(getArticle,trainData))
mapping = []
for i in range(len(trainArticles)):
    for j in range(i+1, len(trainArticles)):
        mapping.append([i,j])

print datetime.datetime.now()
doubleSets = p.map(generateTrainDataPoints,mapping)
print datetime.datetime.now()
trainFeatures = p.map(getFeature,doubleSets)
print datetime.datetime.now()
train(trainFeatures)
print datetime.datetime.now()
print "Training Complete. Now For Testing"

mapping = []
for i in range(len(testArticles)):
    for j in range(i+1, len(testArticles)):
        mapping.append([i,j])

print datetime.datetime.now()
doubleSets = p.map(generateTestDataPoints,mapping)
print datetime.datetime.now()
testFeatures = p.map(getFeature,doubleSets)
print datetime.datetime.now()
test(testFeatures)
print datetime.datetime.now()
print datetime.datetime.now()

#test(generateDataPoints(testArticles))

