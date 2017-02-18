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
listOfYears = []
clf = svm.SVC(probability=True)
probs = []
titles = []
trainData = open('trainDataTitle','r').readlines()
testData = open('testDataTitle','r').readlines()
B = None
#C
def train(features):

    feats = [item[0] for item in features]
    A = len(features)
    B = min(map(len,feats))
    X = np.ones((A,B))
    Y = np.ones((A))
    for feature in range(len(features)):
      print (feature, features[feature][2])
      Y[feature] =  features[feature][2]#label
      for item in range(0,B):
            X[feature][item] = features[feature][0][item]

    clf.fit(X,Y)
    return B

def test(features,B):
    correct = 0
    probs = []
    for feature in features:
        try:
            print feature[2]
        except:
            print feature

        temp = np.array(feature[0][0:B]).reshape((1, -1))
        predict = clf.predict(temp)
        prob = max(clf.predict_proba(temp)[0])
        probs.append([predict,prob, feature[2]])
        #if(feature[1][1] not in G.keys()):
        #    G.update({feature[1][1]:[]})
        #if(feature[1][0] not in G.keys()):
        #    G.update({feature[1][0]:[]})
        #if(predict == 1):
        #    #if(float(prob) > float(0.6)):
        #    G[feature[1][0]].append(feature[1][1])
        #else:
        #    #if(float(prob) > float(0.6)):
        #    G[feature[1][1]].append(feature[1][0])
        if(feature[2] == predict):
            correct +=1
    print "Accuracy = " + str(correct) + '/' + str(len(features))


print datetime.datetime.now()
p = Pool(5)
trainFeatures = []
for i in range(len(trainData)):
    try:
        trainFeatures.append(eval(trainData[i]))
    except:
        print "broken"
B = train(trainFeatures)
print datetime.datetime.now()
#train(generateDataPoints(trainArticles))
print "Training Complere. Now For Testing"

testFeatures = []
for i in testData:
    try:
        testFeatures.append(eval(i))
    except:
        print "broken"
test(testFeatures,B)
print datetime.datetime.now()
