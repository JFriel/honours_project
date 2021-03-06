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
trainData = eval(open('trainDoubleSet','r').readlines()[0])
testData = open('testDoubleSet','r').readlines()

listOfYears = []
clf = linear_model.LogisticRegression()#svm.SVC(probability=True)
probs = []
titles = []

def train(features):
    features = [item for item in features if len(item[0]) != 0]
    feats = [item[0] for item in features]
    A = len(features)
    B = min(map(len,feats))
    X = np.ones((A,B))
    Y = np.ones((A))
    for feature in range(len(features)):
      Y[feature] =  features[feature][2]#label
      for item in range(0,B):
            X[feature][item] = features[feature][0][item]

    clf.fit(X,Y)
    return B

def test(features,B):
    correct = 0
    probs = []
    features = [item for item in features if (len(item[0]) == B)]
    for feature in features:
        temp = np.array(feature[0][0:B]).reshape((1, -1))
        predict = clf.predict(temp[0][0:B])
        #prob = max(clf.predict_proba(temp)[0])
        probs.append([predict, feature[2]])
        if(feature[2] == predict[0]):
            correct +=1
    print "Accuracy = " + str(correct) + '/' + str(len(features))


print datetime.datetime.now()
p = Pool(20)
#Used to get Article Content
#articles = (p.map(getArticle,trainData))
trainFeatures = []
for I in range(len(trainData[0])):
    if trainData[I] is not None:
        trainFeatures.append(trainData[I])
B = train(trainFeatures)
print datetime.datetime.now()
#train(generateDataPoints(trainArticles))
print "Training Complere. Now For Testing"
testData = eval(testData[0])
testFeatures = []
for I in range(len(testData)):
    if testData[I] is not None:
        testFeatures.append(testData[I])
test(testFeatures,B)
