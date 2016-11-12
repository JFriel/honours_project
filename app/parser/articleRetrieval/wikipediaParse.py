import wikipedia

def getArticle(articleName):
    try:
        article=wikipedia.page(articleName)
        return article.content
    except:
        return
