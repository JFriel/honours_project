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
from sklearn import tree, feature_extraction, svm
from sklearn.feature_extraction.text import CountVectorizer
from multiprocessing import Pool
import numpy as np
import datetime

from gensim import corpora
from collections import defaultdict
from pprint import pprint

import app.analytics.filterSentences as fl
import matplotlib.pyplot as plt
G = {}
np.seterr(divide='ignore',invalid='ignore')

trainArticles= open('data/singleShort.txt','r').readlines()#=importArticles.getData('train')
testArticles = open('data/singleShortTest.txt','r').readlines()#= importArticles.getData('test')
print len(trainArticles)
print len(testArticles)
listOfYears = []
clf = svm.SVC(probability=True)
probs = []
titles = []
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
    val = ({'title1':I['title'],'sentences1':I['sentences'],\
            'title2':J['title'],'sentences2': J['sentences'],\
            'year':b, 'vocab':set(sentencesI + sentencesJ)})
    return val
def generateTestDataPoints(tpl):
    X = tpl[0]
    Y = tpl[1]
    doubleSets = []
    I = eval(testArticles[X])
    J = eval(testArticles[Y])
    sentencesI = fl.filter(I['sentences'],I['title'])
    sentencesJ = fl.filter(J['sentences'],J['title'])

    if(I['year'] < J['year']):
        b = 1
    else:
        b = 0
    val = ({'title1':I['title'],'sentences1':I['sentences'],\
            'title2':J['title'],'sentences2': J['sentences'],\
            'year':b, 'vocab':set(sentencesI + sentencesJ)})
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
    print len(X)
    print len(Y)
    print X[0]
    print X[1]
    clf.fit(X,Y)

def test(features):
    correct = 0
    probs = []
    for feature in features:
        temp = np.array(feature[0]).reshape((1, -1))
        predict = clf.predict(temp)
        prob = max(clf.predict_proba(temp)[0])
        probs.append([predict,prob, feature[2]])
        if(feature[1][1] not in G.keys()):
            G.update({feature[1][1]:[]})
        if(feature[1][0] not in G.keys()):
            G.update({feature[1][0]:[]})
        if(predict == 1):
            #if(float(prob) > float(0.6)):
            G[feature[1][0]].append(feature[1][1])    
        else:
            #if(float(prob) > float(0.6)):
            G[feature[1][1]].append(feature[1][0])    
        if(feature[2] == predict):
            correct +=1
    print "Accuracy = " + str(correct) + '/' + str(len(features))

"""stoplist = set('for a of the and to in =='.split())

texts = []
for article in trainArticles:
    a = eval(article)
    b = ' '.join((a['sentences']))
    text = [word for word in b.lower().split() if word not in stoplist]
    texts.append([text,a['year']])

frequency = defaultdict(int)
for text in texts:
    for token in text[0]:
        frequency[token] += 1

#texts = [[token for token in text[0] if frequency[token] > 1]for text in texts]

pprint(texts[0])"""


print datetime.datetime.now()
p = Pool(100)
#Used to get Article Content
#articles = (p.map(getArticle,trainData))
mapping = []
for i in range(len(trainArticles)):
    for j in range(i+1,len(trainArticles)):
        mapping.append([i,j])

print datetime.datetime.now()
doubleSets = p.map(generateTrainDataPoints,mapping)
print datetime.datetime.now()
trainFeatures = p.map(getFeature,doubleSets)

print datetime.datetime.now()
train(trainFeatures)
print datetime.datetime.now()
#train(generateDataPoints(trainArticles))
print "Training Complere. Now For Testing"

mapping = []
for i in range(0,50):#len(testArticles)):
    for j in range(i+1,50):#len(testArticles)):
        mapping.append([i,j])

print datetime.datetime.now()
doubleSets = p.map(generateTestDataPoints,mapping)
print datetime.datetime.now()
testFeatures = p.map(getFeature,doubleSets)
print datetime.datetime.now()
test(testFeatures)
print datetime.datetime.now()

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
           newpaths = find_all_paths(graph, node, end, path)
           for newpath in newpaths:
               paths.append(newpath)
    return paths
"""

keys = G.keys()
start = [None,0]

for k in keys:
    before = len(G[k])
    if before > start[1]:
        start = [k,before]


print datetime.datetime.now()
maxPath = []
for k in range(len(keys)):
    newPaths =  find_all_paths(G,start[0],keys[k])
    for path in newPaths:
        if( len(path) >= len(maxPath)):
            maxPath = path
print maxPath
print len(maxPath)

print datetime.datetime.now()"""
