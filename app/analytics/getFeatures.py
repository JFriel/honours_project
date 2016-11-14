import functions.hasDate as hd
import functions.synonym as sy

def getFeatures(subject, objects, relation, sentences):

    probabilities = []
    foundSentences = []
    usedSentences = []
    synonyms = sy.synonym(relation)
    for sentence in sentences:
        dates=[]
        if 'Retrieved' in sentence:
            next
        try:
            date = hd.hasDate(sentence)
            if (date != []):
                foundSentences.append([sentence,date])
                dates.append(date)
        except:
            next

    total= (len(objects) + 2)* len(foundSentences)
    for s in foundSentences:
        print s
    print '\n\n'

    for (sent,dt) in foundSentences:
        prob = 0
        for obj in objects:
            if (obj in sent):
                prob +=1
        if(subject in sent):
            prob += 1
        for synonym in synonyms:
            if(synonym in sent):
                prob+=1
                break
        probabilities.append(float(prob) / total)

    max_value = max(probabilities)
    max_index = probabilities.index(max_value)

    return probabilities#foundSentences[max_index][1]
