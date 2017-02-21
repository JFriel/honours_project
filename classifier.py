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
trainData = eval(open('/tmp/trainDoubleSet').readlines()[0])#open('trainDataTitle','r').readlines()
testData = open('/tmp/testDoubleSet','r').readlines()
B = None
#C
def train(features):
    features = [item for item in features if len(item[0]) != 0]
    feats = [item[0] for item in features]
    A = len(features)
    B = min(map(len,feats))
    X = np.ones((A,B))
    Y = np.ones((A))
    for feature in range(len(features)):
      #print (features[feature][0], features[feature][2])
      Y[feature] =  features[feature][2]#label
      for item in range(0,B):
            X[feature][item] = features[feature][0][item]

    clf.fit(X,Y)
    return B

def test(features,B):
    correct = 0
    probs = []

    features = [item for item in features if len(item[0]) != 0]
    for feature in features:

        temp = np.array(feature[0][0:B]).reshape((1, -1))
        #temp = temp[0]#[0][0:B]
        predict = clf.predict(temp[0][0:B])
        prob = max(clf.predict_proba(temp[0][0:B])[0])
        probs.append([predict,prob, feature[2]])
        if(feature[2] == predict[0]):
            correct +=1
    print "Accuracy = " + str(correct) + '/' + str(len(features))


print datetime.datetime.now()
p = Pool(5)
trainFeatures = []
print len(trainData)
for i in range(len(trainData)):
    try:
        if trainData[i] is not None:
            trainFeatures.append(trainData[i])
    except:
        print "broken"
B = train(trainFeatures)
print datetime.datetime.now()
#train(generateDataPoints(trainArticles))
print "Training Complere. Now For Testing"

testFeatures = []
testData = eval(testData[0])
for i in range(len(testData)):
    print testData[i]
    try:
        if testData[i] is not None:
            testFeatures.append(testData[i])
    except:
        print "broken"
print len(testFeatures)
test(testFeatures,B)
print datetime.datetime.now()
