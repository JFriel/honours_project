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
from sklearn import tree, feature_extraction, svm, linear_model
from sklearn.feature_extraction.text import CountVectorizer
from multiprocessing import Pool
import numpy as np
import datetime

import app.analytics.filterSentences as fl
import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()

np.seterr(divide='ignore',invalid='ignore')

trainArticles= open('data/singleShort.txt','r').readlines()#=importArticles.getData('train')
testArticles = open('data/singleShortTest.txt','r').readlines()#= importArticles.getData('test')
print len(trainArticles)
print len(testArticles)
listOfYears = []
clf = linear_model.Perceptron(n_iter=12)#svm.SVC(probability=True)
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
    try:
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
    except:
        print "Tuple " + str(tpl) + " Broke."
def getFeature(item):
    yr = item['year']
    vec = fe.get(item['sentences1'],item['sentences2'])
    titles = ([item['title1'],item['title2']])
    return ([vec,titles,yr])
#C
def train(features):
    print features[0]
    X = [item[0] for item in features]
    Y = [item[2] for item in features]
    clf.fit(X,Y)

def test(features):
    correct = 0
    probs = []
    for feature in features:
        temp = np.array(feature[0]).reshape((1, -1))
        predict = clf.predict(temp)
        #prob = max(clf.predict_proba(temp)[0])
        #probs.append([predict,prob, feature[2]])
        G.add_node(feature[1][0])
        G.add_node(feature[1][0])
        if(predict == 1):
            #if(float(prob) > float(0.6)):
            G.add_edge(feature[1][0],feature[1][1])#, weight= prob)

        else:
            #if(float(prob) > float(0.6)):
            G.add_edge(feature[1][1],feature[1][0])#, weight= prob)
        if(feature[2] == predict):
            correct +=1
    print "Accuracy = " + str(correct) + '/' + str(len(features))


print datetime.datetime.now()
p = Pool(20)
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
for i in range(20,len(testArticles)):
    for j in range(i+1,len(testArticles)):
        mapping.append([i,j])

#for i in mapping:
#    if (i[0] == 18 or i[1] ==18):
#        mapping.remove(i)

print datetime.datetime.now()
doubleSets = p.map(generateTestDataPoints,mapping)
print datetime.datetime.now()
testFeatures = p.map(getFeature,doubleSets)
print datetime.datetime.now()
test(testFeatures)
print datetime.datetime.now()

#nx.draw(G, node_color='c',edge_color='k', with_labels=True)

#path = nx.shortest_path(G)
#print path
#path_edges = zip(path,path[1:])
#pos = nx.spring_layout(G)
#nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
#nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=10)
#plt.axis('equal')
#plt.show()
"""
pos = nx.spring_layout(G)
nx.draw(G,pos,node_color='k', with_labels=True)
# draw path in red
largest = max(nx.strongly_connected_components(G), key=len)
print largest
path = nx.dag_longest_path(G)

#print path
path_edges = zip(path,path[1:])

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',edge_labels=labels)

nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.axis('equal')
plt.show()

#plt.show()
#print G.edges()
#print G.nodes()
#T = nx.minimum_spanning_tree(G)
#print sorted(T.edges(data=True))

"""
