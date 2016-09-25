import re

def paragraphs(article, entityList):
    releventParagraphs = []
    paragraphs= [ para.strip('\n') for para in re.split("==.*==",article)]
    for paragraph in paragraphs:
        for entity in entityList:
            if (unicode(entity, "utf-*") in paragraph):
                releventParagraphs.append(paragraph)
                break;

    return releventParagraphs
