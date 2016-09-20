def getData():
    articles = []
    with open('../../data/todayinhistory.txt','r') as f:
        count = 0
        for line in f:
            count +=1
            if(count % 3 == 0):
                articles.append(str(line).strip('\n').split(','))
    return articles
