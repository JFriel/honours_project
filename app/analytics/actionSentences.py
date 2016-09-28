import hasDate as hd

def getActionSentences(actions,paragraph):
    actionSentences = []
    for sentence in paragraph:
        if any(x in sentence for x in actions):
            actionSentences.append(sentence)
        elif(hd.hasDate(sentence) != False):
            actionSentences.append(sentence)
    return actionSentences
