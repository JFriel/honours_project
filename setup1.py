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
from sklearn import tree, feature_extraction
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import datetime
trainArticles= open('singleSets.txt','r')#=importArticles.getData('train')
testArticles = open('singleSetTest.txt','r')#= importArticles.getData('test')
#print len(trainArticles)
listOfYears = []
clf = tree.DecisionTreeClassifier()

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
            listOfYears.append(article[0])
            SS = {'title':article[1], 'sentences':rawSentences, 'year':article[0]}
            singleSets.append(SS)
            print SS
            f.write(SS)
        except:
            pass
    return singleSets
#B
def generateDataPoints(singleSets):
    doubleSets = []
    for i in range(len(singleSets)):
        for j in range(i+1, len(singleSets)):
            if(singleSets[i]['year'] < singleSets[j]['year']):
                b = 1
            else:
                b = 0
            doubleSets.append({'title1':singleSets[i]['title'],'sentences1':singleSets[i]['sentences'],\
                            'title2':singleSets[j]['title'],'sentences2': singleSets[j]['sentences'],\
                            'year':b, 'vocab':set(singleSets[i]['sentences'] + singleSets[j]['sentences'])})

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
        features.append(vec)

    for feature in range(len(features)):
        predict = clf.predict(features[feature])
        prob = clf.predict_proba(features[feature])
        if(prob == bools[feature]):
            correct += 1
        else:
            incorrect +=1

    print "===Accuracy==="
    print "correct : " + str(correct)
    print "Incorrect: " + str(incorrect)

print datetime.datetime.now()
train(generateDataPoints(getArticles(trainArticles)))
print "Training Complere. Now For Testing"

print datetime.datetime.now()

test(generateDataPoints(getArticles(testArticles)))


print datetime.datetime.now()
