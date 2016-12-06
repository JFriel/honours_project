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
from sklearn import tree, feature_extraction
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import datetime
trainArticles= open('singleSets.txt','r').readlines()#=importArticles.getData('train')
testArticles = open('singleSetTest.txt','r').readlines()#= importArticles.getData('test')
doubles = open('doubleSets.txt','r').readlines()
doubleSets = eval(doubles[0])
print len(trainArticles)
print len(testArticles)
listOfYears = []
clf = tree.DecisionTreeClassifier()
probs = []
titles = []
#A
def getArticles(articleList):
    singleSets = []
    for article in articleList:
        try:
            chunks = gc.getChunks(article[1])
            tags =  tag.getTags(article[1],chunks)
            if tags == []:
                continue # check this is right. go to next itteration
            """The Stanford Open IE tags"""
            subject = tags['subject']
            relation = tags['relation']
            objects = tags['object']
            objects = objects.split()

            content = wp.getArticle(subject)
            rawSentences = sent.getSentences(content)
            sentences = []
            for sentence in rawSentences:
                if(hd.hasDate(sentence) !== []):
                    sentences.append(sentence)
            listOfYears.append(article[0])
            SS = {'title':article[1], 'sentences':sentences, 'year':article[0]}
            singleSets.append(SS)
        except:
            pass
    return singleSets
#B
def generateDataPoints(singleSets):
    doubleSets = []
    for i in range(len(singleSets)):
        print str(i) + str(len(singleSets))
        for j in range(i+1, len(singleSets)):
            I = eval(singleSets[i])
            J = eval(singleSets[j])
            if(I['year'] < J['year']):
                b = 1
            else:
                b = 0
            doubleSets.append({'title1':I['title'],'sentences1':I['sentences'],\
                            'title2':J['title'],'sentences2': J['sentences'],\
                            'year':b, 'vocab':set(I['sentences'] + J['sentences'])})

    doubles.write(str(doubleSets))
    print doubleSets
    return doubleSets
#C
def train(doubleSets):
    bools = []
    features = []

    for item in doubleSets:
        bools.append(item['year'])
        vec = fe.get(item['sentences1'],item['sentences2'])
        features.append(vec)
    print "Training The Classifier."
    clf.fit(features,bools)

def test(doubleSets):
    bools = []
    features = []
    correct = 0
    incorrect = 0
    for item in doubleSets:
        bools.append(item['year'])
        vec = fe.get(item['sentences1'],item['sentences2'])
        titles.append([item['title1'],item['title2']])
        features.append(vec)

    for feature in range(len(features)):
        predict = clf.predict(features[feature])
        prob = clf.predict_proba(features[feature])
        probs.append([predict,prob, bools[feature]])
        #if(prob == bools[feature]):
        #    correct += 1
        #else:
        #    incorrect +=1

    #print "===Accuracy==="
    #print "correct : " + str(correct)
    #print "Incorrect: " + str(incorrect)
print "beginning training"
train(doubleSets)
print "Training Complere. Now For Testing"


test(generateDataPoints(testArticles))

print zip(titles,probs)

