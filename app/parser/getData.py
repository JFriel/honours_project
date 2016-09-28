import os

def getData():
    articles = []
    with open( './data/todayinhistory.txt','r') as f:
        count = 0
        for line in f:
            try:
                count +=1
                if(count % 3 == 0):
                    line = line.decode('utf-8')
                    articles.append(str(line).strip('\n').split(','))
            except:
                print "Cant read this article"
    return articles
