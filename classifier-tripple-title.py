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
from sklearn import tree, feature_extraction, svm, linear_model, neural_network
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

clf = neural_network.MLPClassifier()#svm.SVC(probability=True)#tree.DecisionTreeClassifier()
titles = []
weights = []

G = {}#nx.DiGraph()#G is an empty graph


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
        SS = {'title':article[1], 'sentences':article[0], 'year':article[0]}
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
    titleI = fl.filter(I['title'],I['title'])
    titleJ = fl.filter(J['title'],J['title'])
    titleK = fl.filter(K['title'],K['title'])
    if(I['year'] < J['year'] < K['year']):
        b = 1
    elif( I['year'] > J['year'] > K['year']):
        b = 0
    else:
        b = -1
    val = ({'title1':I['title'],'title1':I['title'],\
            'title2':J['title'],'title2': J['title'],\
            'title3':K['title'],'title3': K['title'],\
            'year':b, 'vocab':set(titleI +  titleJ + titleK)})
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
    elif( I['year'] > J['year'] > K['year']):
        b = 0
    else:
        b = -1
    val = ({'title1':I['title'],'title1':I['title'],\
            'title2':J['title'],'title2': J['title'],\
            'title3':K['title'],'title3': K['title'],\
            'year':b, 'vocab':set(I['title'] + J['title'] + K['title'])})
    return val

def getFeature(item):
    yr = item['year']
    vec = fe.get3(item['title1'],item['title2'], item['title3'])
    titles = ([item['title1'],item['title2'],item['title3']])
    return ([vec,titles,yr])
#C
def train(features):
    print features
    X = [ item[0] for item in features]
    Y = [item[2] for item in features]
    clf.fit(X,Y)
    B = min(map(len,X))
    return B

def test(features,B):
    correct = 0
    labels = []
    predictions = []
    features = [item for item in features if len(item[0]) != 0]
    for feature in features:
        temp = np.array(feature[0][0:B]).reshape((1, -1))
        predict = clf.predict(temp[0][0:B].reshape((1,-1)))
        #prob = max(clf.predict_proba(temp)[0])
        #add all articles to G
        if(feature[1][1] not in G.keys()):
            G.update({feature[1][1]:[]})
            #H.update({feature[1][1]:feature[2]})
        if(feature[1][0] not in G.keys()):
            G.update({feature[1][0]:[]})
            #H.update({feature[1][0]:feature[2]})
        #Add list of which came before what
        if(predict == 1):
            G[feature[1][0]].append(feature[1][1])
            labels.append(1)
            predictions.append(feature[-1])
        else:
            G[feature[1][1]].append(feature[1][0])
            labels.append(0)
            predictions.append(feature[-1])

        #probs.append([predict, feature[2]])
        if(feature[2] == predict[0]):
            correct +=1
    print ("Accuracy = " + str(correct) + '/' + str(len(features)))




p = Pool(10)
#Used to get Article Content
#articles = (p.map(getArticle,trainData))

#mapping = itertools.combinations(range(len(trainArticles)),3)
mapping = []
for i in range(len(trainArticles)):
    for j in range(i+1, 50):#len(trainArticles)):
        for k in range(j+1, 50):#len(trainArticles)):
            mapping.append([i,j,k])
print datetime.datetime.now()

#tripleSets = []
#for i in range(len(mapping)):
#    print i
#    tripleSets.append(generateTrainDataPoints(mapping[i]))
tripleSets = p.map(generateTrainDataPoints,mapping[0:30])
for i in tripleSets:
    if(float(i['year']) == float(-1)):
        tripleSets.remove(i)

print datetime.datetime.now()
#print tripleSets[0]
trainFeatures = p.map(getFeature,tripleSets)
print datetime.datetime.now()
B = train(trainFeatures)
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
for i in doubleSets:
    if(i['year'] == -1):
        doubleSets.remove(i)
print datetime.datetime.now()
testFeatures = p.map(getFeature,doubleSets)
print datetime.datetime.now()
test(testFeatures,B)
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

#nx.draw(G, node_color='c', edge_color='k', with_labels=True)
#nx.dfs_edges(G)
#plt.show()
print (G)
#test(generateDataPoints(testArticles))
