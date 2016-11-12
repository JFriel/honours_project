import functions.hasDate as hd
import functions.synonym as sy

def getFeatures(subject, objects, relation, sentences):
    synonyms = sy.synonym(relation)
    features = []
    foundSentences = []
    usedSentences = []
    for sentence in sentences:
        dates=[]
        try:
            date = hd.hasDate(sentence)
            if (date != []):
                foundSentences.append([sentence,date])
                dates.append(date)
        except:
            next

    for (sent,dt) in foundSentences:
        for obj in objects:
            if (obj in sent and sent not in usedSentences):
                features.append([sent,dt])
                usedSentences.append(sent)
    return features
