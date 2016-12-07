import tag

def filter(sentences,title):
    returnSentences = []
    tags = tag.getTags(title,None)
    if tags == []:
        return [title]
    else:
        """The Stanford Open IE tags"""
        subject = tags['subject']
        relation = tags['relation']
        objects = tags['object']
        objects = objects.split()
    for sentence in sentences:
        if(subject in sentence):
            returnSentences.append(sentence)

    return returnSentences
