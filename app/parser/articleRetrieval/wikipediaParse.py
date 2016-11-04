import wikipedia

def getArticle(articleName):
    try:
        return wikipedia.summary(articleName)
    except:
        return
