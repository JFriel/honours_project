import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import app.parser.getData as importArticles
import app.parser.articleRetrieval.getArticles as getContent
import app.parser.sentences as sent
import app.analytics.features as fe
from sklearn import tree, feature_extraction, svm, linear_model, neural_network
from sklearn.feature_extraction.text import CountVectorizer
from multiprocessing import Pool
import numpy as np
import datetime

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

import app.analytics.filterSentences as fl
import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()

np.seterr(divide='ignore',invalid='ignore')

listOfYears = []
clf = neural_network.MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2),random_state=1)
probs = []
titles = []
trainData = open('trainData','r').readlines()
testData = open('testData','r').readlines()

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
        #prob = max(clf.predict_proba(temp)[0])
        probs.append([predict, feature[2]])
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
p = Pool(20)
trainFeatures = []
for I in trainData:
    try:
        trainFeatures.append(eval(I))
    except:
        print ""
B = train(trainFeatures)
print datetime.datetime.now()
#train(generateDataPoints(trainArticles))
print "Training Complere. Now For Testing"
testFeatures = []
for I in testData:
    try:
        testFeatures.append(eval(I))
    except:
        print ""
test(testFeatures,B)
