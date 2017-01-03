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
from sklearn import tree, feature_extraction, svm
from sklearn.feature_extraction.text import CountVectorizer
from multiprocessing import Pool
import numpy as np
import datetime
import itertools
import networkx as nx
import matplotlib.pyplot as plt


np.seterr(divide='ignore',invalid='ignore')

trainArticles= open('data/singleShort.txt','r').readlines()#=importArticles.getData('train')
testArticles = open('data/singleShortTest.txt','r').readlines()#= importArticles.getData('test')
print len(trainArticles)
print len(testArticles)
listOfYears = []


testArticleLookupDict = {}
for title in range(0,len(testArticles)):
    #print (eval(testArticles[title])['title'])
    testArticleLookupDict[eval(testArticles[title])['title']] = title

clf = svm.SVC(probability=True)#tree.DecisionTreeClassifier()
titles = []
weights = []

G = nx.DiGraph()#G is an empty graph


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
    Z = tpl[2]
    doubleSets = []
    I = eval(trainArticles[X])
    J = eval(trainArticles[Y])
    K = eval(trainArticles[Z])
    sentencesI = fl.filter(I['sentences'],I['title'])
    sentencesJ = fl.filter(J['sentences'],J['title'])
    sentencesK = fl.filter(K['sentences'],K['title'])
    if(I['year'] < J['year'] < K['year']):
        b = 1
    else:
        b = 0
    val = ({'title1':I['title'],'sentences1':I['sentences'],\
            'title2':J['title'],'sentences2': J['sentences'],\
            'title3':K['title'],'sentences3': K['sentences'],\
            'year':b, 'vocab':set(sentencesI +  sentencesJ + sentencesK)})
    return val
def generateTestDataPoints(tpl):
    X = tpl[0]
    Y = tpl[1]
    Z = tpl[2]
    doubleSets = []
    I = eval(testArticles[X])
    J = eval(testArticles[Y])
    K = eval(testArticles[Z])
    if(I['year'] < J['year'] < K['year']):
        b = 1
    else:
        b = 0
    val = ({'title1':I['title'],'sentences1':I['sentences'],\
            'title2':J['title'],'sentences2': J['sentences'],\
            'title3':K['title'],'sentences3': K['sentences'],\
            'year':b, 'vocab':set(I['sentences'] + J['sentences'] + K['sentences'])})
    return val

def getFeature(item):
    yr = item['year']
    vec = fe.get3(item['sentences1'],item['sentences2'], item['sentences3'])
    titles = ([item['title1'],item['title2'],item['title3']])
    return ([vec,titles,yr])
#C
def train(features):
    print features
    X = [ item[0] for item in features]
    Y = [item[2] for item in features]
    clf.fit(X,Y)


def test(features):
    correct = 0
    for feature in features:
        predict = clf.predict(np.array([feature[0]]))
        prob = clf.predict_proba(np.array([feature[0]]))
        prob = prob[0][predict][0]
        title1 = feature[1][0]
        title2 = feature[1][1]
        title3 = feature[1][2]
        #print "title1 = " + str(title1)
        #print prob
        #print str(title1) + "," + str(title2) + "," + str(float(prob))
        G.add_edge(str(title1),str(title2), weight=float(prob))
        G.add_edge(str(title1),str(title3), weight=float(prob))
        G.add_edge(str(title2),str(title3), weight=float(prob))
        if(feature[2] == predict):
            correct +=1
    print "Accuracy = " + str(correct) + '/' + str(len(features))




p = Pool(10)
#Used to get Article Content
#articles = (p.map(getArticle,trainData))

#mapping = itertools.combinations(range(len(trainArticles)),3)
mapping = []
for i in range(len(trainArticles)):
    for j in range(i+1, len(trainArticles)):
        for k in range(j+1, len(trainArticles)):
            mapping.append([i,j,k])
print datetime.datetime.now()

#tripleSets = []
#for i in range(len(mapping)):
#    print i
#    tripleSets.append(generateTrainDataPoints(mapping[i]))
tripleSets = p.map(generateTrainDataPoints,mapping[0:3000])
print datetime.datetime.now()
#print tripleSets[0]
trainFeatures = p.map(getFeature,tripleSets)
print datetime.datetime.now()
train(trainFeatures)
print datetime.datetime.now()
print "Training Complete. Now For Testing"

#mapping = itertools.combinations(range(len(testArticles)),3)
mapping = []
for i in range(len(testArticles)):
    for j in range(i+1, len(testArticles)):
        for k in range(j+1, len(testArticles)):
            mapping.append([i,j,k])
            
print datetime.datetime.now()
doubleSets = p.map(generateTestDataPoints,mapping)
print datetime.datetime.now()
testFeatures = p.map(getFeature,doubleSets)
print datetime.datetime.now()
test(testFeatures)
print datetime.datetime.now()
print datetime.datetime.now()

Data = []
for t in testArticles:
    Data.append(eval(t))


def graph(ttl):
    T = nx.bfs_tree(G,ttl)


    edgeAccuracy = 0
    years = []
    for e in T.edges():
        t1 = e[0]
        t2 = e[1]
        y1 = 0
        y2 = 0
        for d in Data:
            if(d['title'] == t1):
                y1 = d['year']
            if(d['title'] == t2):
                y2 = d['year']
        #print e
        #print str(y1) + " | " + str(y2)
        if(y1 > y2):
            edgeAccuracy += 1
        if(years == []):
            years.append(y1)
            years.append(y2)
        else:
            years.append(y2)

    yearsAccuracy = 0
    for y in range(1,len(years)):
        if( years[y] > years[y-1]):
            yearsAccuracy +=1

    print(T.edges())
    #print years
    #print "edge Accuracy = " + str(edgeAccuracy)
    print ttl + " = " + str(yearsAccuracy)
    
#for d in Data:
#graph("1st magazine on microfilm offered to subscribers - Newsweek")

nx.draw(G, node_color='c', edge_color='k', with_labels=True)
nx.dfs_edges(G)
plt.show()
#test(generateDataPoints(testArticles))
