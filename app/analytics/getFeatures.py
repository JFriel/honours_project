import functions.hasDate as hd

def getFeatures(subject, objects, sentences):
    features = []
    for sentence in sentences:
        for obj in objects:
            if (obj or subject) in sentence:
                try:
                    date = hd.hasDate(sentence)
                    if (date != []):
                        features.append([sentence,obj,date])
                        break
                except:
                    next
    return len(features)
