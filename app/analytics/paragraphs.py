import re
from nltk import tokenize

def paragraphs(article, entityList):
    releventParagraphs = []
    paragraphs= [ para.strip('\n') for para in re.split("==.*==",article[1])]
    print article[0]
    print entityList
    for paragraph in paragraphs:
        for entity in entityList:
            if entity == article[0]:
                pass
            if (unicode(entity, "utf-*") in paragraph):
                paragraphSentences = tokenize.sent_tokenize(paragraph)
                releventParagraphs.append(paragraphSentences)
                break;

    return releventParagraphs
