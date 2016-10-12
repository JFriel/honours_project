import wikipedia

def getArticle(articleName):
    try:
        return wikipedia.page(articleName).content
    except:
        return
