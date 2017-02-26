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

import app.analytics.filterSentences as fl
import matplotlib.pyplot as plt
import networkx as nx
G = {}
np.seterr(divide='ignore',invalid='ignore')

trainArticles= eval(open('bigSingleSets','r').readlines()[0])[1:200]#=importArticles.getData('train')
testArticles= eval(open('bigSingleSets','r').readlines()[0])[2000:2050]#=importArticles.getData('train')
listOfYears = []
clf = svm.SVC(probability=True)
probs = []
titles = []
#A

#B
def generateTrainDataPoints(tpl):
    X =tpl[0]
    Y = tpl[1]
    doubleSets = []
    I = (trainArticles[X])
    J = (trainArticles[Y])
    if I is None or J is None:
        return
    try:
        #sentencesI = I[#fl.filter(I['sentences'],I['title'])
        #sentencesJ = #fl.filter(J['sentences'],J['title'])
        #print type(sentencesI)
        if(I['year'] < J['year']):
            b = 1
        else:
            b = 0
        val = ({'title1':I['title'],'sentences1':I['sentences'],\
                'title2':J['title'],'sentences2': J['sentences'],\
                'year':b, 'vocab':set(I['sentences'] + J['sentences'])})
        return val
    except:
        return
def generateTestDataPoints(tpl):
    X = tpl[0]
    Y = tpl[1]
    doubleSets = []
    I = eval(testArticles[X])
    J = eval(testArticles[Y])
    #sentencesI = fl.filter(I['title'],I['title'])
    #sentencesJ = fl.filter(J['title'],J['title'])

    if(I['year'] < J['year']):
        b = 1
    else:
        b = 0
    val = ({'title1':I['title'],'sentences1':I['sentences'],\
            'title2':J['title'],'sentences2': J['sentences'],\
            'year':b, 'vocab':set(I['sentences'] + J['sentences'])})
    return val

def getFeature(item):
    if item is None:
        return
    yr = item['year']
    vec = fe.get(item['sentences1'],item['sentences2'])
    titles = ([item['title1'],item['title2']])
#    print [vec,titles,yr]
    return ([vec,titles,yr])
#C

p = Pool(30)
#Used to get Article Content
#2articles = (p.map(getArticle,trainData))
mapping = []
for i in range(len(trainArticles)):
    for j in range(i,len(trainArticles)):
            mapping.append([i,j])

doubleSets = p.map(generateTrainDataPoints,mapping)

#print "making train features"
#print len(doubleSets)
#print "finished Doubles"
#for item in doubleSets:
#    if item is not None:
#        getFeature(item)

trainFeatures = p.map(getFeature,doubleSets)
print trainFeatures
#print trainFeatures
#train(trainFeatures)
#print datetime.datetime.now()
#train(generateDataPoints(trainArticles))
#print "Training Complere. Now For Testing"
"""
mapping = []
for i in range(0,len(testArticles)):
    for j in range(i+1,len(testArticles)):
        mapping.append([i,j])

doubleSets = p.map(generateTestDataPoints,mapping)
testFeatures = p.map(getFeature,doubleSets)
#test(testFeatures)
#print datetime.datetime.now()
"""
"""
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

print datetime.datetime.now()
print G
#nx.draw_networkx(G,with_lables=True)
#plt.show()"""
