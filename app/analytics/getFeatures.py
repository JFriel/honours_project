import functions.hasDate as hd
import functions.synonym as sy
import short_sentence_similarity as sim

def getFeatures(article, sentences,subject):

    probabilities = []
    foundSentences = []
    usedSentences = []
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
    for (sent,date) in foundSentences:
        if(subject in sent):
            probabilities.append(sim.similarity(article,sent,True))
    """total= (len(objects) + 2)* len(foundSentences)
    for s in foundSentences:
        print s

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
    """
    try:
        max_value = max(probabilities)
        max_index = probabilities.index(max_value)
    except:
        return 'NO USEFUL SENTENCES'
    #[x for y, x in sorted(zip(foundSentences, probabilites))]
    return sorted(zip(probabilities,foundSentences), reverse=True)#foundSentences[max_index]
