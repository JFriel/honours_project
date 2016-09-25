import wikipediaParse as wikipedia

def getArticles(entities):
    articles = []
    for entity in entities:
        content = wikipedia.getArticle(entity)
        articles.append(content)

    return articles
