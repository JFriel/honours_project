import wikipedia

def getArticle(articleName):
    return wikipedia.page(articleName).content
