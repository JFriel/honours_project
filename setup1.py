import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import app.parser.getData as importArticles
import app.parser.articleRetrieval.getArticles as getContent
import app.parser.sentences as sent
import app.parser.getChunks as gc
import app.analytics.tag as tag
import app.parser.articleRetrieval.wikipediaParse as wp
import app.analytics.featureExtraction as fe
from sklearn import tree, feature_extraction
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

articles=importArticles.getData()

singleSets=[]
doubleSets = []
#A
for article in articles[0:10]:
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
        sentences= fe.featureExtraction(rawSentences)
        singleSets.append({'title':article[1], 'sentences':sentences, 'year':article[0]})
    except:
        pass
#B

for i in range(len(singleSets)):
    for j in range(i+1, len(singleSets)):
        if(singleSets[i]['year'] < singleSets[j]['year']):
            b = 1
        else:
            b = 0
        doubleSets.append({'title1':singleSets[i]['title'],'sentences1': singleSets[i]['sentences'],'title2':singleSets[j]['title'],'sentences2': singleSets[j]['sentences'], 'year':b})

#C
bools = []
features = []

for item in doubleSets:
    bools.append(item['year'])
    vec = feature_extraction.DictVectorizer()
    vec.fit_transform([item['sentences1'], item['sentences2']]).toarray()
    features.append(vec)

X = np.array(features)
Y = np.array(bools)

#print type(features)
print type(features[0])
#print type(features[0][0])
#print type(features[0][0][0])

#Need to let it take i a dict or something)
clf = tree.DecisionTreeClassifier()
print 'begining fit' + str(time.time())
clf=clf.fit(X,Y)

print 'completed fit' + str(time.time())

