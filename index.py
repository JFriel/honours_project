import app.parser.ner as ner
import app.parser.getData as importArticles

articles = importArticles.getData()

for article in articles[0:5]:
    print ner.NER(article[1])
    print('\n\n\n')
